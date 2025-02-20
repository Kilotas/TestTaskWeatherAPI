from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import WeatherAPIView, RegisterView

urlpatterns = [
    path('weather/<str:city>/', WeatherAPIView.as_view(), name='weather'),
    path('register/', RegisterView.as_view(), name='register'),
]
