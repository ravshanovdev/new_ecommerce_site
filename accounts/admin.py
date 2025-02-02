from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "phone", "is_active", "is_staff", "is_superuser"]


admin.site.register(CustomUser, CustomUserAdmin)



