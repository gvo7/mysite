from django.contrib import admin
from .models import Integrator, Type, Vendor, Product, Device, Configuration_owner, Management

# Register your models here.
admin.site.register(Integrator)
admin.site.register(Type)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Device)
admin.site.register(Configuration_owner)
admin.site.register(Management)