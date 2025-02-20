from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Weather
from .serializers import WeatherSerializer, RegisterSerializer
import requests
from django.utils.timezone import now
from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission

API_KEY = "9b35f7dd5905f333be760bf1db2d97d4"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



class RegisterView(APIView):
    """
    Регистрация нового пользователя.
    """

    @extend_schema(
        summary="Регистрация нового пользователя",
        description="Создает нового пользователя и добавляет его в группу 'Пользователь'.",
        request=RegisterSerializer,
        responses={
            201: RegisterSerializer,
            400: OpenApiResponse(description="Ошибка валидации данных")
        }
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Просто сохраняем пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class WeatherAPIView(APIView):
    #permission_classes = []
    @extend_schema(
        summary="Получение погоды по городу",
        description="Запрашивает погоду по указанному городу. Если данные устарели или отсутствуют, делает запрос к внешнему API.",
        responses={
            200: WeatherSerializer,
            400: OpenApiResponse(description="Ошибка: не удалось получить данные о погоде")
        }
    )
    def get(self, request, city):
        weather = Weather.objects.filter(city=city).first()

        if weather and weather.is_fresh():
            serializer = WeatherSerializer(weather)
            return Response(serializer.data)

        # Данных нет или устарели — запрашиваем у API (передаем название города, ключ, температуру в градусах цельсия и на русском запрашиваем описание)
        response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"})

        # проверяем успешен ли http запрос
        if response.status_code == 200:
            data = response.json() # конвертируем наш ответ с api
            weather_data = {
                "temperature": data["main"]["temp"], # температура
                "description": data["weather"][0]["description"], #описание погоды
            }
            # если город уже есть в базе данных, обновляем последние новости о нем
            if weather:
                weather.temperature = weather_data["temperature"]
                weather.description = weather_data["description"]
                weather.last_updated = now()
                weather.save()
            # если города нет, то добавляем его в нашу базу данных
            else:
                weather = Weather.objects.create(city=city, **weather_data)

            # с помощью сериализатора переводим его в json формат
            serializer = WeatherSerializer(weather)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "Не удалось получить данные о погоде"}, status=status.HTTP_400_BAD_REQUEST)

