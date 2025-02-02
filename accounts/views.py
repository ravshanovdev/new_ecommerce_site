from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
User = get_user_model()


class RegistrationApiView(APIView):

    def post(self, request):
        phone = request.data["phone"]
        password = request.data["password"]

        user = User(phone=phone)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "success",
                "user_id": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        )


# class LoginApiView(APIView):
#
#     def post(self, request):
#         phone = request.data['phone']
#         password = request.data['password']


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]



