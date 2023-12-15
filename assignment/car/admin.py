from django.contrib import admin
from car.models import Car, Brand, Order,Comment
# Register your models here.
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(Comment)