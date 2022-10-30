from django.shortcuts import redirect
from posts.models import Post
from django.views.generic import ListView, CreateView


class PostListView(ListView):
    template_name: str = 'posts/index.html'
    model = Post
    context_object_name = 'posts'


class PostCreateView(CreateView):
    template_name = 'posts/post_add.html'
    model = Post
    fields = ['image', 'description', 'author']
    success_url = '/'
