from django.urls import path
from .views import *

urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='create_order'),
    path('delete_all/', delete_all_orders, name='delete_all_orders'),
]
