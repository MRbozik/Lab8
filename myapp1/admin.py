from django.contrib import admin
from .models import Clients, Cars, Repairs

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    pass

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    pass

@admin.register(Repairs)
class RepairsAdmin(admin.ModelAdmin):
    pass