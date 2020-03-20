from django.conf import settings
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/', customer, name='customer'),
]
