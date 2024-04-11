from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from intern_app.views import *





urlpatterns = [
    
    path('api/register/', RegisterView.as_view(), name ='register-api'),
    path('api/login/', LoginView.as_view(), name = 'login-api'),
    path('api/refresh/', TokenRefresh.as_view(), name = 'refresh-api'),


    
]