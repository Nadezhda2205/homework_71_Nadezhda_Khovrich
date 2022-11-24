from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        exclude = ('liked_users', 'commented_users')
