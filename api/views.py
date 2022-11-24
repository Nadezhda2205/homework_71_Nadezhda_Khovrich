from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from api.serializers import PostSerializer
from api.permissions import IsOwner


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None
        if (handler and self.permission_classes_per_method and self.permission_classes_per_method.get(handler.__name__)):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)
        super().check_permissions(request)


class PostApiView(PermissionPolicyMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes_per_method = {
        'create': [IsAuthenticated, IsOwner],
        'like_post': [IsAuthenticated],
        'unlike_post': [IsAuthenticated],
        'destroy': [IsAuthenticated, IsOwner],
        'update': [IsAuthenticated, IsOwner],
        'partial_update': [IsAuthenticated, IsOwner]
    }


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
