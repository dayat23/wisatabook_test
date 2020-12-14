from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('books/', views.BookStoreListView.as_view(), name='books'),
]
