from rest_framework import serializers
from .models import Users, Shops, Items, Orders, CartItems, Reviews


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["username", "password", "email", "address", "contact_number", "is_admin"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users(
            email=validated_data['email'],
            username=validated_data['username'],
            address=validated_data['address'],
            contact_number=validated_data['contact_number'],
            is_admin=validated_data['is_admin']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"
