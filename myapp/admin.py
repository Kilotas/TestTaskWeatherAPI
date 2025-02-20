from django.contrib import admin
from .models import Weather
admin.site.register(Weather) ## импортируем Weather, если хотим добавить у себя в базе данных информацию о погоде
# Register your models here.
