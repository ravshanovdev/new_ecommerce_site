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


# update product

class UpdateProductApiView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)

            if product and product.user == request.user:
                serializer = ProductSerializer(product, data=request.data)

                if serializer.is_valid():
                    serializer.save(user=request.user)
                    return Response(serializer.data, status.HTTP_200_OK)
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

            else:
                return Response("Product Not Found", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# detail Product

class DetailProductApiView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)

            if product:
                serializer = ProductSerializer(product)
                return Response(serializer.data, status.HTTP_200_OK)
            return Response("Product Not Found", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductListApiView(APIView):
    def get(self, request):
        try:
            product = Product.objects.all()

            if product:
                serializer = ProductSerializer(product, many=True)
                return Response(serializer.data)
            return Response("Products Not Created Yet", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# delete Product

class DeleteProductApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk, user=request.user)

            if product:
                product.delete()

                return Response("Product was Successfully Deleted", status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response("Product Not Found", status.HTTP_404_NOT_FOUND)


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
                serializer.save(user=request.user)
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


# list your orders

class ListYourOrdersApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            order = Orders.objects.filter(user=request.user)

            if order:
                serializer = OrdersSerializer(order, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            return Response("You have not any order", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"exception": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# delete your orders

class DeleteOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, reqeust, pk):
        try:
            order = Orders.objects.get(pk=pk, user=reqeust.user)

            order.delete()
            return Response("Order Was Successfully Deleted", status.HTTP_200_OK)

        except Orders.DoesNotExist:
            return Response({"exception": "Orders Not Found"}, status.HTTP_404_NOT_FOUND)
