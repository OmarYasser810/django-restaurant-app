from django.shortcuts import render, redirect
from .models import Order, OrderItem
from menu.models import MenuItem

# Create your views here.
def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone_number')
        items = request.POST.getlist('items')
        quantities = request.POST.getlist('quantities')
        order = Order.objects.create(customer_name=customer_name, phone=phone)
        
        for item_id, quantity in zip(items, quantities):
            if quantity and int(quantity) > 0:
                item = MenuItem.objects.get(item_id=item_id)  # <-- use item_id here
                OrderItem.objects.create(order=order, item=item, quantity=int(quantity))
        return redirect('order_list')
    menu_items = MenuItem.objects.all()
    return render(request, 'create_order.html', {'menu_items': menu_items})
        
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})

def delete_all_orders(request):
    Order.objects.all().delete()
    return redirect('order_list')