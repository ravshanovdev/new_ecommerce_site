from django.urls import path
from .views import CreateOrdersApiView, CreateCartApiView, CreatePaymentApiView, UpdatePaymentApiView, \
    PaymentDetailApiView

urlpatterns = [
    path('create_cart/', CreateCartApiView.as_view(), ),
    path("create_order/", CreateOrdersApiView.as_view(), ),
    path("create_payment", CreatePaymentApiView.as_view(), )

]
