from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    sitze = models.TextField(verbose_name='Размеры', blank=True, null=True)
    color1 = models.TextField(max_length=100)
    color2 = models.TextField(max_length=100)
    color3 = models.TextField(max_length=100)
    descr = models.TextField()
    price = models.IntegerField()
    class Meta:
        verbose_name = 'Изделия'
        verbose_name_plural = 'Изделия'
    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    tel = models.PositiveIntegerField(verbose_name='Телефон')
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
    def __str__(self):
        return self.name
