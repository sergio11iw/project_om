from .views import *
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('contacts', contacts, name='contacts'),
    path('produkts', produkts, name='produkts'),
    path('produkt/search', produkt_search, name='produkt_search'),
    path('produkt_list/<int:list_id>', produkt_list, name='list'),
    path('feedback/', feedback, name='feedback'),
    path('create-order/', create_order, name='create_order'),
    path('add_to_cart/<int:note_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart_view'),  # Убедитесь, что это имя совпадает
    path('remove_from_cart/<int:note_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:note_id>/', update_cart, name='update_cart'),  # Для обновления количества

]