from django.urls import path 
from .views import RegisterUserAPIView 
from .views import BlogListCreateAPIView, BlogReriveUpdateDestroyAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
]

urlpatterns += [
    path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogReriveUpdateDestroyAPIView.as_view(), name='blog-detail'),
]