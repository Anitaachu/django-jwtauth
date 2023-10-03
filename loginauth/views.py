from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from . models import UserData
from rest_framework.response import Response
from rest_framework import response, status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny


# view for registering users
class RegisterView(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer
    Permission_classes = (AllowAny,)
    

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
