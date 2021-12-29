from django.http import JsonResponse
from django.contrib.auth import login
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Users, Shops, Items, CartItems, Orders, Reviews
from .serializers import UserSerializer, ShopSerializer, CartItemsSerializer, \
    ItemSerializer, OrderSerializer, ReviewsSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer


def hello(request):
    return JsonResponse({
        "message": "Health check"
    }, status=200)


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        user = request.user
        return Response(self.get_serializer(user).data, status=200)


class ShopsViewSet(ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopSerializer


class CartItemsViewSet(ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer


class ItemsViewSet(ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer


class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

