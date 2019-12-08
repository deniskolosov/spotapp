from django.contrib import admin
from .models import Customer, Order, Product, Producer

admin.site.register(Customer)
admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Order)
