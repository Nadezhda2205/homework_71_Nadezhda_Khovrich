from django.contrib import admin
from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['description', 'image', 'author']
    ordering = ['-created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'text']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
