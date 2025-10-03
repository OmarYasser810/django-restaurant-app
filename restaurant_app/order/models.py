# from django.db import models
# from restaurant_app.customer.models import Customer
# from restaurant_app.menu.models import Item

# # Create your models here.
# class Order(models.Model):
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name="orders"   # lets us access customer.orders.all()
#     )
#     customer_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     created_at = models.DateTimeField(auto_now_add=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(
#         "Order",
#         on_delete=models.CASCADE,
#         related_name="order_items"
#     )
#     item = models.ForeignKey(
#         "menu.item_id",
#         on_delete=models.CASCADE
#     )
#     quantity = models.PositiveIntegerField(default=1)
    