from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer
import subprocess


def hello(request):
    return JsonResponse({
        "message": "Inside docker"
    }, status=200)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Todo(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(http_method_names=["POST"])
def execute_code(request):
    subprocess.call("g++ code/abcd.cpp")
    subprocess.call("./a.exe")
    return JsonResponse({
        "message": "Done"
    }, status=200)


@api_view(http_method_names=["POST"])
def divide_numbers(request):
    num1 = request.data["num1"]
    num2 = request.data["num2"]
    return JsonResponse({
        "message": num1/num2
    }, status=200)