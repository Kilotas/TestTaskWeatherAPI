from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.timezone import now


class User(AbstractUser): # наследуемся от abstract user, чтобы была возможность использовать стандартные поля
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    city = models.CharField(max_length=100)  # Город пользователя
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username


class Weather(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    last_updated = models.DateTimeField(default=now)

    def is_fresh(self):
        return (now() - self.last_updated).total_seconds() < 600  # просчитываем 10 минут с последнего обновления
