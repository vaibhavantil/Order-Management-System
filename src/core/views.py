from django.shortcuts import render
from django.http import HttpResponse

from . models import *

# Query the required objects
# Set them up into the Context
# Pass them into the templates section


def index(request):
    # customers = Customer.objects.all()
    # orders = Order.objects.all()
    # context = {'customers': customers, 'orders': orders}
    # return render(request, 'index.html', context)
    return render(request, 'index.html', {})


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'customers': customers, 'orders': orders, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'dashboard.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def customer(request):
    return render(request, 'customer.html', {})
