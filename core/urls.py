from .views import *
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('produkts', produkts, name='produkts'),
    path('produkt_list/<int:list_id>', produkt_list, name='list'),
    path('feedback/', feedback, name='feedback'),



]