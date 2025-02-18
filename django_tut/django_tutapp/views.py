from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Student, MyUser
from .serializers import StudentSerializer, MyUserSerializer
from django.db.models import Q
from django.contrib.auth import get_user_model  # For custo User Model

User = get_user_model()

# Create your views here.
class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        re_password = request.data.get('re_password')
        
        if not username or not password or not email:
            return Response({'error':'Username, Password and Email are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response({'error': 'Username or Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not (password == re_password) or len(password) < 8:
            return Response({'error': 'Password and Re-Password are Not matched or length of password is too short'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'msg':'User created successfully', 'data':'{}.format(user)'}, status=status.HTTP_201_CREATED)        
        
        
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer