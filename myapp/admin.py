from django.contrib import admin
from .models import Person, Car, Driver, Client, Employee
# Register your models here.

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Employee)



