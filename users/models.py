from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    points_count= models.PositiveIntegerField(default=0, verbose_name='Кол-во балов')
    color = models.CharField(default="white",max_length=30, verbose_name='Цвет')
    passed_tests= models.PositiveIntegerField(default=0, verbose_name='Кол-во пройденых тестов')

    # color = models.CharField(default='#FF0000')

    def __str__(self):
        return self.color
