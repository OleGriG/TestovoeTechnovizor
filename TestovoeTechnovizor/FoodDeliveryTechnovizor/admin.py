from django.contrib import admin
from .models import Employee, Dish, Order


admin.site.register(Employee)
admin.site.register(Order)

admin.site.register(Dish)
