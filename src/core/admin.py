from django.contrib import admin
from django.contrib.auth.models import Group


# Register your models here.
from .models import *

# admin.site.unregister(Groups)
admin.site.unregister(Group)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
