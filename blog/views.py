from django.shortcuts import render
from .models import Orders, Category, Product, Payments, Cart, CartItems
from .serializer import ProductSerializer, OrdersSerializer, CartSerializer, CategorySerializer, \
    CartItemsSerializer, PaymentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


# CART
# Create Cart

class CreateCartApiView(APIView):
    def post(self, request):
        try:
            serializer = CartSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors)

        except Exception as e:
            return Response({"exception": e})


# ORDERS
# Create Orders

class CreateOrdersApiView(APIView):
    def post(self,request):
        try:
            serializer = OrdersSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors)

        except Exception as e:
            return Response({"exception": e})


# PAYMENT
# Create Payment

class CreatePaymentApiView(APIView):
    def post(self, request):
        try:
            serializer = PaymentsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"exception": e})


# Update Payment

class UpdatePaymentApiView(APIView):
    def put(self, request):
        try:
            serializer = PaymentsSerializer(Payments, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"exception": e})


# payment detail

class PaymentDetailApiView(APIView):
    def get(self, request):
        try:
            payment = Payments.objects.filter(user=request.user)

            if payment:
                serializer = PaymentsSerializer(payment, many=True)
                return Response(serializer.data)
            return Response("You have not any payment")

        except Exception as e:
            return Response({"exception": e})


# delete payment

# class DeletePaymentApiView(APIView):
#     def delete(self, request):
#         try:
#             user =


