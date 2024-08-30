from django.urls import path

from .views import ViewPost, ViewPostById, DeletePost, CreatePost

urlpatterns = [
    path('view/', ViewPost.as_view()),
    path('view/<int:pk>/', ViewPostById.as_view()),
    path('delete/<int:pk>/', DeletePost.as_view()),
    path('create/', CreatePost.as_view()),
]