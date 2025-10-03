from django.urls import path
from .views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('insert/', insert_menu_item, name='insert_menu_item'),
    path('edit/<int:item_id>/', edit_menu_item, name='edit_menu_item'),
    path('delete/<int:item_id>/', delete_menu_item, name='delete_menu_item'),
]
