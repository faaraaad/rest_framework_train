from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .serializers import CreateUserSerializer, CommentSerializer, SimpleSerializer, CreateUserSerializer2
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomeAuth, TestAuth
from .models import CommentModel, SimpleModel
from django.utils.decorators import method_decorator
from rest_framework.decorators import action, permission_classes, authentication_classes
from rest_framework import viewsets, status
from rest_framework.throttling import UserRateThrottle


class TestShow(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, CustomeAuth]

    def get(self, request, who):
        return Response({'user': str(request.user), 'auth':str(request.auth)})

    def post(self, request,who):
        print(type(request.data))
        return Response({'name': request.data['name'], 'family': request.query_params['value'],'who': who})


class CreateUser(APIView):
    def post(self, request):
        validation = CreateUserSerializer(data=request.data)
        if validation.is_valid():
            vd = validation.validated_data
            User.objects.create_user(username=vd['username'], password=vd['password'], email=vd['email'])
            return Response({'value': 'successful'})
        return Response(validation.errors)


class CustomThrottle(UserRateThrottle):
    rate = '15/day'


class HomeView(APIView):
    throttle_scope= 'InamCustom'
    throttle_classes= [CustomThrottle]

    @staticmethod
    def get(self, request):
        posts= CommentModel.objects.all()
        data= CommentSerializer(instance=posts, many=True).data
        return Response(data)


class PostDetail(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes= [IsAuthenticated, CustomeAuth]

    def get(self, request, post_id):
        objects= CommentModel.objects.filter(user= request.user)
        self.check_object_permissions(request, objects.first())
        obj_ser= CommentSerializer(instance=objects, many=True).data
        return Response(obj_ser)


class RouterTestViewset(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TestAuth, IsAuthenticated]
    queryset = SimpleModel.objects.all()

    def create(self, request):
        data = SimpleSerializer(data= request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = self.queryset.get(pk= pk)
        ss= SimpleSerializer(instance =instance, data = request.data)
        if ss.is_valid():
            ss.save()
            print(request.headers)
            return Response(status=status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        srz_data= CreateUserSerializer2(data= request.data)
        if srz_data.is_valid():
            print(srz_data.validated_data)
            srz_data.save()
            return Response(status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)    

