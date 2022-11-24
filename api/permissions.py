from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, post):
        if request.user == post.author:
            return True
        return False
        