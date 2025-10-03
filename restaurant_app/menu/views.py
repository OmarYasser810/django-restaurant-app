from django.shortcuts import render, redirect
from .models import MenuItem

# Create your views here.
def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def insert_menu_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        photo = request.FILES.get('photo')

        MenuItem.objects.create(
            name=name,
            category=category,
            description=description,
            price=price,
            photo=photo
        )
        return redirect('insert_menu_item')
    return render(request, 'insert_menu_item.html')

def edit_menu_item(request, item_id):
    item = MenuItem.objects.get(item_id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.category = request.POST.get('category')
        item.description = request.POST.get('description')
        item.price = request.POST.get('price')
        if 'photo' in request.FILES:
            item.photo = request.FILES.get('photo')
        item.save()
        return redirect('menu')
    return render(request, 'edit_menu_item.html', {'item': item})

def delete_menu_item(request, item_id):
    item = MenuItem.objects.get(item_id=item_id)
    item.delete()
    return redirect('menu')