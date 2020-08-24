from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    customers = Customers.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
            'customers': customers, 
            'orders':orders,
            'total_customers':total_customers,
            'total_orders':total_orders,
            'delivered':delivered,
            'pending':pending

            }

    return render(request, 'dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products' : products })

def customers(request, pk):
    customers = Customers.objects.get(id=pk)
    orders = customers.order_set.all()
    order_count = orders.count()

    context = {'customers': customers, 'orders':orders, 'order_count':order_count}

    return render(request, 'customers.html', context)
