from rest_framework import serializers
from .models import Orders, Category, Product, Payments, Cart, CartItems
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "phone"]


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Payments
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    user_identifier = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "ordered", "user_identifier", "total_price"]


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"

        


