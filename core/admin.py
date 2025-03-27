from django.contrib import admin
from .models import Note, User, ShopUser, Order, OrderItem
admin.site.register(Note)
admin.site.register(User)
admin.site.register(ShopUser)
admin.site.register(Order)
admin.site.register(OrderItem)