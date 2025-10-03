from django.urls import path
from .views import *

urlpatterns = [
    path('', menu_view, name='menu'),
    path('insert/', insert_menu_items, name='insert_menu_items'),
]
