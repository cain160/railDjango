from django.contrib import admin

# Register your models here.
from Railserve.models import Device
from Railserve.models import Position


admin.site.register(Device)
admin.site.register(Position)
