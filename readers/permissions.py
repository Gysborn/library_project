from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return bool(request.user and request.user.is_staff)
