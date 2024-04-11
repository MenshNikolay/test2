from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RefTokenSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from intern_app.utils import refresh_token

from intern_app.models import RefToken
import uuid




class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []  
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Need to cheak not adding new line to db
class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []  
    permission_classes = [AllowAny]


    def post(self,request,*args, **kwargs):    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.data['email']
        user_objct = User.objects.filter(email=email).first()
        password = request.data.get('password')
        

        user = authenticate(request, username=user_objct.username, password=password)
        

        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = refresh_token()
            RefToken.objects.create(user=user, ref_token=token)
            return Response({
                    'access_token': str(refresh.access_token),
                    'refresh_token' : str(token),
                    }) 
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class TokenRefresh(generics.CreateAPIView):
        serializer_class = RefTokenSerializer
        authentication_classes = []    
        permission_classes = []


        def post(self,request,*args, **kwargs): 
            ref_token = request.data.get('ref_token')
            if not ref_token:
                 return Response({"error":"Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                obj = RefToken.objects.get(ref_token=ref_token)
            except RefToken.DoesNotExist:
                return Response({'error': 'Token does not exist'}, status=status.HTTP_404_NOT_FOUND)
            
                

            new_token = uuid.uuid4()
            
            
            obj.ref_token = new_token
            obj.save()
            refresh = RefreshToken.for_user(obj)

            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': new_token,
            }, status=status.HTTP_201_CREATED)
            
            
             