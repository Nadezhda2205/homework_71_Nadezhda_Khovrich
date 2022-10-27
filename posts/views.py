from django.shortcuts import render
from posts.models import Post
from django.views.generic import ListView


class PostListView(ListView):
    '''просмот списка проектов, 
    dispatch - проверка на добавление задачи пользователю именно этого проекта'''
    template_name: str = 'base.html'
    model = Post
    context_object_name = 'projects'