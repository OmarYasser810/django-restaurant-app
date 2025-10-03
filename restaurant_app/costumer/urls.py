from django.urls import path
from .views import *

urlpatterns = [
    path('', customer, name='customer'),
    path('insert/', insert_customer, name='insert_customer'),
    path('edit/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete/<int:customer_id>/', delete_customer, name='delete_customer'),
]
