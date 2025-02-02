from django.contrib import admin
from .models import Product, Orders, Cart, CartItems, Category, Payments


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "cart_id", "delivery_method", "location", "full_name", "phone", "status"]


admin.site.register(Orders, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "price", "description", "image_url", "category_id"]


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Category, CategoryAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user_identifier", "total_price", "ordered"]


admin.site.register(Cart, CartAdmin)


class CartItemsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "cart_id", "product_id", "quantity", "price"]


admin.site.register(CartItems, CartItemsAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "order_id", "payment_method", "screenshot_url", "status"]


admin.site.register(Payments, PaymentAdmin)

