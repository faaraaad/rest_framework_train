from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CommentModel
from rest_framework.response import Response
import json


def unique_email(useremail):
    if User.objects.filter(email=useremail).exists():
        raise serializers.ValidationError('choose another email')
    return useremail


def admin_check(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin too emailete')
    return value

class CreateUserSerializer(serializers.ModelSerializer):
    password2= serializers.CharField()
    class Meta:
        model= User
        fields=('username','email' ,'password', 'password2')
        extra_kwargs={
            'email': {'validators': [admin_check, unique_email], 'required': True}}

    def validate_username(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('admin na')
        return value
        
    def validate(self, data):
        if data['password']!= data['password2']:
            raise serializers.ValidationError('passwords must match dadash')
        return data    
        
        
class CommentSerializer(serializers.ModelSerializer):
    subcomment= serializers.SerializerMethodField()
    class Meta:
        model= CommentModel
        fields= ['body', 'is_reply', 'from_comment','user', 'subcomment']
    def get_subcomment(self,obj):
        if obj.subcomment:
            return CommentSerializer(instance= obj.subcomment.all(),many=True).data
