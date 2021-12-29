from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserViewSet)
router.register("shop", views.ShopsViewSet)
router.register("cart", views.CartItemsViewSet)
router.register("item", views.ItemsViewSet)
router.register("order", views.OrdersViewSet)
router.register("review", views.ReviewsViewSet)
urlpatterns = [
    path("", views.hello, name="health"),
    path("login/", views.LoginView.as_view()),
]

urlpatterns += router.urls
