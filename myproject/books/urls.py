from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books_list, name='list'),
    path('add/', views.book_create, name='book_add'),
    path('filtered/', views.books_list_filtered, name='books_list_filtered'),
    path('<slug:slug>/', views.book_page, name='book'),
]