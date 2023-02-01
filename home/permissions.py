from rest_framework import permissions
from django.contrib.auth.models import User


class CustomeAuth(permissions.BasePermission):
    message='you are not farhad babe'
    def has_permission(self, request, view):
        user= User.objects.filter(username= 'farhad').get()
        return request.user==user
