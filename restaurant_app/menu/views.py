from django.shortcuts import render, redirect
from .models import MenuItem

# Create your views here.
def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def insert_menu_items(request):
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
        return redirect('insert_menu_items')
    return render(request, 'insert_menu_items.html')