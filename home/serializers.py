from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CommentModel, SimpleModel, ProfileModel
from rest_framework.response import Response
from drf.mongo import get_cursor


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
    # subcomment= serializers.SerializerMethodField()
    supcomment= serializers.SerializerMethodField()
    # user= serializers.StringRelatedField(read_only=False)
        
    class Meta:
        model= CommentModel
        fields= ['body', 'is_reply', 'from_comment','user', 'supcomment']
    # def get_subcomment(self,obj):
    #     if obj.subcomment:
    #         return CommentSerializer(instance= obj.subcomment.all(),many=True).data
    def get_supcomment(self, obj):
        try:
            sd= CommentSerializer(instance=obj.from_comment).data
        except:
            sd= {}
        return sd









class TestiMongo(serializers.Serializer):
    name= serializers.CharField(max_length= 10)
    family= serializers.CharField(default= 'asadi')
    def create(self):
        pass

    def validate(self, data):
        if data['name']=='farhad':
            raise serializers.ValidationError('o o o, no no')
        return data

class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model= SimpleModel
        fields= ['name', 'family', 'is_ok']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProfileModel
        fields= ['address']

class CreateUserSerializer2(serializers.ModelSerializer):
    password2=serializers.CharField(max_length= 30)
    address=serializers.CharField(required= False)
    #address= AddressSerializer()
    class Meta:
        model= User
        fields= ['username', 'password', 'email', 'password2', 'address']

    def validate(self, values):
        if values['password2'] != values['password']:
            raise serializers.ValidationError('passwords are not match with each other')
        return values
    def create(self, validated_data):
        address = validated_data.pop('address')
        del validated_data['password2']
        user= User.objects.create_user(**validated_data)
        ProfileModel.objects.create(user_profile= user, address= address)
        return user