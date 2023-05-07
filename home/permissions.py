from rest_framework import permissions
from django.contrib.auth.models import User


class CustomeAuth(permissions.BasePermission):
    message='you are not farhad'

    def has_permission(self, request, view):
        user = User.objects.filter(username='farhad').get()
        return request.user == user

    def has_object_permission(self, request, view, obj):
        if request.METHOD in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class TestAuth(permissions.BasePermission):
    message= 'you are not valid honey'

    def has_permission(self, request, view):
        print(view)
        return request.query_params.get('value', None) != 'farhad'