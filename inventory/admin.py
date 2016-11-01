from __future__ import unicode_literals
from django.contrib import admin
from .models import Team, Service_status, Location, Integrator, Type, Vendor, Product, Device, Configuration_owner, Management

# Register your models here.
admin.site.register(Team)
admin.site.register(Service_status)
admin.site.register(Location)
admin.site.register(Integrator)
admin.site.register(Type)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Device)
admin.site.register(Configuration_owner)
admin.site.register(Management)