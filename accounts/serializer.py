from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    phone = serializers.CharField()

    def validate(self, attrs):
        phone = attrs.get("phone")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError("Telefon raqami noto‘g‘ri!")

        if not user.check_password(password):
            raise serializers.ValidationError("Parol noto‘g‘ri!")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user_id": user.id
        }
