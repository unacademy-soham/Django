from rest_framework.permissions import BasePermission
from .models import Users, Shops
import logging

logger = logging.getLogger("")


class AdminPermissions(BasePermission):

    def has_permission(self, request, view):
        user = Users.objects.get_by_natural_key(username=request.user.username)
        if request.method in ["POST", "PATCH", "DELETE"]:
            return user.is_admin
        return True

    def has_object_permission(self, request, view, obj):
        # For shop user attribute is available
        # For cart user attribute is not available
        print("Here")
        print(type(obj) == type(Shops))
        print(obj.user.username == request.user.username)
        print(obj.user.username)
        if request.method in ["PATCH", "DELETE"]:
            if type(obj) == type(Shops):
                if obj.user.username == request.user.username:
                    return True
                else:
                    return False
        return True
