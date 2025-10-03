from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.
def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def insert_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Customer.objects.create(name=name, email=email, phone=phone)

        return redirect('customer')  # Redirect to a success page or customer list

    return render(request, 'insert_customer.html')

def edit_customer(request, customer_id):
    from .models import Customer
    customer = Customer.objects.get(id=customer_id)

    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.save()
        return redirect('customer')  # Redirect to a success page or customer list

    return render(request, 'edit_customer.html', {'customer': customer})

def delete_customer(request, customer_id):
    from .models import Customer
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect('customer')  # Redirect to a success page or customer list