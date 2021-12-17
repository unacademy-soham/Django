from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer
from .tasks import add, thumbnail_creator_task
import uuid
import subprocess
import os
from PIL import Image


def hello(request):
    env = os.environ.get("ENV", "None")
    return JsonResponse({
        "message": "Hi I am Soham. Environment: " + env
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
    add.delay(num1, num2)
    return JsonResponse({
        "message": "Successfully submitted"
    }, status=200)


@api_view(http_method_names=["POST"])
def create_thumbnail(request):
    file = request.FILES.get("file")
    file_id = str(uuid.uuid4())
    image = Image.open(file)
    image.save("images/" + file_id + ".jpg")
    thumbnail_creator_task.delay(file_id)
    return JsonResponse({
        "message": "Processing the file"
    }, status=200)
