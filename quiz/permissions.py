from rest_framework import permissions

"""Razreshaetsya esli nasha sessiya sovpadaet. Inache drugoi ne mojet smotret' chujie dannye"""

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.user == request.user

