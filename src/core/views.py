from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})


def products(request):
    return HttpResponse('products')


def customer(request):
    return HttpResponse('customer')
