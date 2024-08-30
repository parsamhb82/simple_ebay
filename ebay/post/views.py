from django.shortcuts import render
from django.http import JsonResponse
from post.models import Post
from costumer.models import Costumer
from .serializers import PostSerializer
import json
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView



class ViewPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ViewPostById(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 
class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

