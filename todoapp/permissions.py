from rest_framework.permissions import BasePermission


class AdminPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["POST", "PATCH", "DELETE"]:
            return request.user.is_admin
        return True

    def has_object_permission(self, request, view, obj):
        # For shop user attribute is available
        # For cart user attribute is not available
        if request.method in ["PATCH", "DELETE"]:
            if obj.__class__.__name__ == "Shop":
                if obj.user == request.user:
                    return True
            else:
                return False
        return True
