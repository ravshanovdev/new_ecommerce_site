from django.urls import path
from .views import CreateOrdersApiView, CreateCartApiView, UpdateOrderApiView, DetailOrderApiView, \
    CreateCategoryApiView, CreateProductApiView

urlpatterns = [
    # urls cart
    path('create_cart/', CreateCartApiView.as_view(), ),
    # urls order
    path("create_order/", CreateOrdersApiView.as_view(), ),
    path("update_order/<int:pk>/", UpdateOrderApiView.as_view(), ),
    path("detail_order/<int:pk>/", DetailOrderApiView.as_view(), ),
    # urls category
    path("create_category/", CreateCategoryApiView.as_view(), ),
    # urls product
    path("create_product/", CreateProductApiView.as_view(), ),

]
