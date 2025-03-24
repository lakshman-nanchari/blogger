from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password
from .models import Blog 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, }}
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['passeord'])
        return super().create(validated_data)

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Blog 
        fields = ['id', 'title', 'content', 'author', 'created_at']

