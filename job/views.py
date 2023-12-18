from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class registrationview(APIView):
    def post(self, request):
        serializer = registrationserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }
            return Response(response, status=201)
        return Response(serializer.errors, status=400)
        
class login(APIView):
    def post(self, request):
        print(request)
        email = request.data.get('email')
        password = request.data.get('password')
        user = registrationModel.objects.filter(email=email,password=password).first()
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=401)