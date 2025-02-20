from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Weather

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'city']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        city = validated_data.pop("city", None)
        user = User.objects.create_user(**validated_data)
        if city:
            user.city = city
            user.save()
        return user

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
