from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer


def hello(request):
    return JsonResponse({
        "message": "Hello welcome to todoapp"
    }, status=200)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Todo(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


