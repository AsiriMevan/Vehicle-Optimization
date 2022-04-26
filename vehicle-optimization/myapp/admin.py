from django.contrib import admin

# Register your models here.
from .models import Client,Client_deliveries,Client_history,Warehouse,Warehouse_deliveries,Warehouse_history,Warehouse_vehicles,Vehicle

admin.site.register(Client)
admin.site.register(Client_deliveries)
admin.site.register(Client_history)
admin.site.register(Warehouse)
admin.site.register(Warehouse_deliveries)
admin.site.register(Warehouse_history)
admin.site.register(Warehouse_vehicles)
admin.site.register(Vehicle)