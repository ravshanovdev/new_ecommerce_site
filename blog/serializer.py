from rest_framework import serializers
from .models import Orders, Category, Product, Payments, Cart, CartItems
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "Username"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Payments
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"

        


