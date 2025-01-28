from django.contrib import admin
from .models import Product, Orders, Cart, CartItems, Category, Payments

admin.site.register([Product, Orders, Cart, CartItems, Category, Payments])
