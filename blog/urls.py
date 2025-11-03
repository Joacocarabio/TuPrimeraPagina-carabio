# blog/urls.py
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', views.home, name='home'),                         # /
    path('about/', views.about, name='about'),                 # /about/
    path('pages/', PostListView.as_view(), name='post_list'),  # /pages/
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('pages/create/', PostCreateView.as_view(), name='post_create'),
    path('pages/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('pages/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search/', views.search_posts, name='post_search'),
]
