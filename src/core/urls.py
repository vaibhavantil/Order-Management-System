from django.conf import settings
from django.urls import path

from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),
]
