from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})
    def validate(self, data):
        if not data:
            raise serializers.ValidationError("Empty payload")
        return data



class ContentCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    tag = serializers.CharField()

    class Meta:
        model = ContentTable
        fields = ['id', 'title','content','tag']

    def validate(self, data):
        if not data:
            raise serializers.ValidationError("Empty payload")
        return data

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagTable
        fields = ['id', 'title']


class ContentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='created_by.username', read_only=True)
    tag_title = serializers.CharField(source='tag.title', read_only=True)
    timestamp = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        model = ContentTable
        fields = ['id', 'title', 'content', 'timestamp', 'user_name', 'tag_title']
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagTable
        fields = ['id', 'title']
