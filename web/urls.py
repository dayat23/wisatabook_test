from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search', views.AutocompleteView.as_view(), name='search'),
]
