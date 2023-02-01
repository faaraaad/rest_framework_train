from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import CommentModel


# Register your models here.

# @admin.register(User)
# class SiteUser(admin.ModelAdmin):
#     fields=['username', 'email']


admin.site.register(CommentModel)