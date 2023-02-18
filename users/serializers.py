from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import Project

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'name', 'email', 'phone', 'password')


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'username', 'name', 'email',
                  'phone', 'projects', 'password')


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'owner', 'description', 'date_created')


# class ScriptSerializer(ModelSerializer):
#     class Meta:
#         model = Script
#         fields = ('id', 'name', 'project', 'nodes',
#                   'edges', 'data', 'date_created')
