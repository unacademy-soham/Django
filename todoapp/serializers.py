from rest_framework import serializers
from .models import User, Todo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Todo
        fields = "__all__"
