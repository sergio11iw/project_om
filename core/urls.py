from .views import *
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('contacts', contacts, name='contacts'),
    path('adminus', adminus, name='adminus'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('produkts', produkts, name='produkts'),
    path('produkt/search', produkt_search, name='produkt_search'),
    path('change_order_status/<str:model_name>/<int:object_id>/', change_order_status, name='change_order_status'),
    path('produkt_list/<int:list_id>', produkt_list, name='list'),
    path('feedback/', feedback, name='feedback'),
    path('create-order/', create_order, name='create_order'),
    path('create-order-cart/', create_order_cart, name='create_order_cart'),
    path('add_to_cart/<int:note_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart_view'),
    path('remove_from_cart/<int:note_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:note_id>/', update_cart, name='update_cart'),
    path('order-success/', order_success_view, name='order_success'),

    # Для обновления количества

]