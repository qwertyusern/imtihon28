

from django.contrib import admin
from django.urls import path
from app1.views import *
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('suvlar/', Suvlar.as_view()),
    path('mijozlar/', Mijozlar.as_view()),
    path('buyurtmalar/', BuyurtmaApi.as_view()),
    path('haydovchilar/', HaydovhilarApi.as_view()),
    path('haydovchi/<int:pk>', HaydovchiApi.as_view()),
    path('adminlar/', AdminlarApi.as_view()),
    path('admin/<int:pk>', AdminApi.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Spotify Api",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Xojiakbar Goipov. Email:<xojiakbargoipov3@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)