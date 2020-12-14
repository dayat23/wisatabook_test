from rest_framework import serializers

from board.models import BookStore


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class BookStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookStore
        fields = ('title', 'short_summary', 'published_date')
