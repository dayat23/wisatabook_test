from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.db.models import Q

# import models
from django.contrib.auth.models import User
from board.models import BookStore

# import serializer
from .serializers import BookStoreSerializer, LoginSerializer


class LoginView(CreateAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @staticmethod
    def generate_token(user):
        refresh = RefreshToken.for_user(user)
        data = {
            'status': 1,
            'msg': 'login success',
            'token': str(refresh.access_token),
        }
        return data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        try:
            u = User.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
            if u.check_password(password):
                data = self.generate_token(u)
                return Response(data, status=status.HTTP_200_OK)
            data = {'status': 0, 'msg': 'Invalid email or password.'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            data = {'status': 0, 'msg': 'Email not registered'}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as err:
            data = {'status': 0, 'msg': str(err)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookStoreListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookStoreSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = BookStore.objects.all()
        if q:
            pass
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
