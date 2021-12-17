from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserViewSet)
router.register("todo", views.Todo)

urlpatterns = [
    path("", views.hello, name="hello"),
    path("execute", views.execute_code, name="execute"),
    path("divide", views.divide_numbers, name="divide"),
    path("thumbnail", views.create_thumbnail, name="create_thumbnail")
]

urlpatterns += router.urls