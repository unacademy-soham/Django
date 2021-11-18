from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserViewSet)
router.register("todo", views.Todo)

urlpatterns = [
    path("", views.hello, name="hello"),
    path("execute", views.execute_code, name="execute")
]

urlpatterns += router.urls