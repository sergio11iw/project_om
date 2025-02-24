from django.contrib import admin
from .models import Note, User, ShopUser
admin.site.register(Note)
admin.site.register(User)
admin.site.register(ShopUser)