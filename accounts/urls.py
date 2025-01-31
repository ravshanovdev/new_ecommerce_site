from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import RegistrationApiView, CustomTokenObtainPairView

urlpatterns = [

    path("api/register/", RegistrationApiView.as_view(), ),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("api/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

