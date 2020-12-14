from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.db.models import F

from board.models import BookStore


class HomeView(TemplateView):
    template_name = 'home.html'


class AutocompleteView(View):

    def dispatch(self, request, *args, **kwargs):
        q = self.request.GET.get('q')
        queryset = BookStore.objects.values(value=F('title'), data=F('title')).filter(title__contains=q)
        results = {
            "query": "Unit",
            "suggestions": list(queryset)
        }
        return JsonResponse(results)
