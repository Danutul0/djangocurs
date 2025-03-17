from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name ="list"),
    path('add/', views.movie_create, name ="movie_add"),
    path('<slug:slug>/', views.movies_page, name ="movie"),
]
