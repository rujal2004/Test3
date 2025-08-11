import secrets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User,Chat
from .serializers import UserSerializer,ChatSerializer
from django.contrib.auth.hashers import make_password,check_password

# Helper - authenticate by token
def authenticate_user(token):
    try:
        return User.objects.get(auth_token = token)
    except User.DoesNotExist:
        return None
    
##  Task1 - Registration
class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            if User.objects.filter(username=username).exists():
                return Response({"error":"Username already exists"},status=status.HTTP_400_BAD_REQUEST)
            
            user = User(username=username,password =make_password(password))
            user.save()
            return Response({"message":"Registration successful","tokens":user.tokens},
                           status=status.HTTP_201_CREATED )
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
# TASK 2 -LOGIN
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        if not user or not check_password(password,user.password):
            return Response({"error":"Invalid credintials"},status = status.HTTP_401_UNAUTHORIZED)
        
        token =secrets.token_hex(16)
        user.auth_token =token
        user.save()
        return Response({"message":"Login successfull","auth_token":token})
    


# Task 3 - Chat API

class ChatView(APIView):
    def Post(self,request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({"error":"Authorization token required"},status = status.HTTP_401_UNAUTHORIZED)
        user = authenticate_user(token)
        if not user:
            return Response({"error":"Invalid token"},status=status.HTTP_401_UNAUTHORIZED)
        
        if user.tokens<100:
            return Response({"error":"Not enough tokens"},status=status.HTTP_400_BAD_REQUEST)
        
        message = request.data.get('message')
        if not message:
            return Response({"error":"message is required"},status=status.HTTP_400_BAD_REQUEST)
        
        
        ## Dummy ai response
        response_text = f"ai response to:{message}"
        
        # Save Chat
        
        Chat.objects.create(user = user,message=message,response=response_text)
        
        ## Deduct tokens
        user.tokens -=100
        user.save()
        
        return Response({"message":message,"response":response_text,"remaining_tokens":user.tokens})
    
    
    
    ## Task -4 Token Balance 
    
class TokenBalanceView(APIView):
    def get(self,request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({"error":"Authorization token required"},status=status.HTTP_401_UNAUTHORIZED)           
            
        user = authenticate_user(token)
        if not user:
            return Response({"error":"Invalid token"},status=status.HTTP_401_UNAUTHORIZED)
            
        return Response({"tokens":user.tokens})