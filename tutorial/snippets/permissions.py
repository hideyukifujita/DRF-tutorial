from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """request, objを受け取って、requestメソッドがSAFE_METHODSに等しい
        or ownerとuserが等しいならTrueを返す

        Args:
            request (HttpRequest): HttpRequestオブジェクト
            view (_type_): _description_
            obj (dict): Snippetオブジェクト

        Returns:
            bool: True or False
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user