from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserViewSet)
router.register("todo", views.Todo)

urlpatterns = [
    path("", views.hello, name="hello")
]

urlpatterns += router.urls