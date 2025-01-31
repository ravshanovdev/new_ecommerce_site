from django.shortcuts import render
from .models import Orders, Category, Product, Payments, Cart, CartItems
from .serializer import ProductSerializer, OrdersSerializer, CartSerializer, CategorySerializer, \
    CartItemsSerializer, PaymentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Category

class CreateCategoryApiView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# PRODUCT
# Create Product

class CreateProductApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)

            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






# CART
# Create Cart


class CreateCartApiView(APIView):
    def post(self, request):
        try:
            if request.user.is_authenticated:
                serializer = CartSerializer(data=request.data)

                if serializer.is_valid():
                    serializer.save(user_identifier=request.user)
                    return Response(serializer.data, status.HTTP_201_CREATED)
                return Response(serializer.errors)
            else:
                return Response("You must signup or login", status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ORDERS
# Create Orders

class CreateOrdersApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = OrdersSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors)


        except Exception as e:

            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# update order

class UpdateOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:

            order = Orders.objects.get(pk=pk)
            if request.user != order.user:
                return Response("Not Found", status.HTTP_404_NOT_FOUND)

            serializer = OrdersSerializer(order, data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# detail order

class DetailOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = Orders.objects.get(pk=pk)

        if order.user != request.user or not order:
            return Response("Not Found", status.HTTP_404_NOT_FOUND)

        serializer = OrdersSerializer(order)

        return Response(serializer.data)
