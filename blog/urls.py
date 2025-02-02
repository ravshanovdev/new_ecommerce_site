from django.urls import path
from .views import CreateOrdersApiView, CreateCartApiView, UpdateOrderApiView, DetailOrderApiView, \
    CreateCategoryApiView, CreateProductApiView, UpdateProductApiView, DetailProductApiView, \
    ProductListApiView, DeleteProductApiView, ListYourOrdersApiView, DeleteOrderApiView

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
    path("update_product/<int:pk>/", UpdateProductApiView.as_view(), ),
    path("get_product/<int:pk>/", DetailProductApiView.as_view(), ),
    path("products_list/", ProductListApiView.as_view(), ),
    path("delete_product/<int:pk>/", DeleteProductApiView.as_view(), ),
    path("get_your_orders/", ListYourOrdersApiView.as_view(), ),
    path("delete_order/<int:pk>/", DeleteOrderApiView.as_view(), ),






]
