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
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    tel = models.PositiveIntegerField(verbose_name='Телефон')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_date']
    def get_status_label(self):
        for key, label in self.STATUS_CHOICES:
            if key == self.status:
                return label
        return None  # Если статус не найден
    def __str__(self):
        return self.name

class ShopUser (models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    tel = models.PositiveIntegerField(verbose_name='Телефон')
    product_name = models.CharField(verbose_name='Изделие', max_length=255, null=True, blank=True)
    product_color = models.CharField(verbose_name='Цвет', max_length=255, null=True, blank=True)
    product_count = models.CharField(verbose_name='Кол-во', max_length=255, null=True, blank=True)
    product_total = models.CharField(verbose_name='Сумма', max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_date']
    def get_status_label(self):
        for key, label in self.STATUS_CHOICES:
            if key == self.status:
                return label
        return None  # Если статус не найден

    def __str__(self):
        return self.name




class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=15)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заказ с корзины'
        verbose_name_plural = 'Заказы с корзины'
        ordering = ['-created_date']
    def __str__(self):
        return f"Order {self.id} by {self.name}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Note, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of Product {self.product_id} in Order {self.order.id}"


