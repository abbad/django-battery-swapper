from django.contrib import admin
from shifts.models import Shift, VehicleShift 


class VehicleShiftAdmin(admin.TabularInline):
    model = VehicleShift


class ShiftAdmin(admin.ModelAdmin):
    inlines = [
        VehicleShiftAdmin,
    ]

    model = Shift

admin.site.register(Shift, ShiftAdmin)
