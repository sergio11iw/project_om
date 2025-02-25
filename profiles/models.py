from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name='Картинка', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    tel = models.PositiveIntegerField(verbose_name='Телефон', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

