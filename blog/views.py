from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User
from .models import Blog 
from .serializers import UserSerializer, BlogSerializer
from rest_framework.permissions import AllowAny 
# Create your views here.

class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListCreateAPIView(generics.ListCreateAPIView):
    quesryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogReriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 
    permission_classes = [permissions.IsAuthenticated]