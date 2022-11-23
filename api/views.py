from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse

from posts.models import Post
from api.serializers import PostSerializer



class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def like_post(self, request, *args, **kwargs):
        post_by_pk = self.get_object()
        user_from_request = request.user
        post_by_pk.liked_users.add(user_from_request)
        return JsonResponse({'key': 'aaaaa'})
    
    def unlike_post(self, request, *args, **kwargs):
        post_by_pk = self.get_object()
        user_from_request = request.user
        post_by_pk.liked_users.remove(user_from_request)
        return JsonResponse({'key': 'aaaaa'})
