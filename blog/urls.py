from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/new/', views.post_create, name='post_create'),
    path('search/', views.post_search, name='post_search'),
    path('authors/new/', views.author_create, name='author_create'),
    path('categories/new/', views.category_create, name='category_create'),
]
