import email
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=255)
    client_description = models.TextField()
    email = models.EmailField(max_length=255)
    contact_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=255)
    client_priority = models.CharField(max_length=255)
    geofence_details = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'clients'

    def __str__(self):
        return self.client_name

class Vehicle(models.Model):
    vehicle_Id = models.CharField(max_length=255)
    vehicle_Brand = models.CharField(max_length=255)
    vehicle_Number = models.CharField(max_length=255)
    vehicle_Type = models.CharField(max_length=255)
    scheduled_Date = models.DateField()
    scheduled_Location = models.CharField(max_length=255)
    designated_Driver = models.CharField(max_length=255)
    warehouse = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'vehicle'

    def __str__(self):
        return self.vehicle_Id

class Client_deliveries(models.Model):
    client = models.ForeignKey(Client, related_name='client_deliveries', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_creator1')
    scheduled_deliveries = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'client_deliveries'
        ordering = ('-scheduled_deliveries',)
    
    def save(self, *args, **kwargs):
        super(Client_deliveries, self).save(*args, **kwargs) 

 
class Client_history(models.Model):
    client = models.ForeignKey(Client, related_name='client_history', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_creator')
    history_deliveries = models.ForeignKey(Client_deliveries, on_delete=models.CASCADE, related_name='history')

    class Meta:
        verbose_name_plural = 'clients_history'
        ordering = ('-history_deliveries',)



class Warehouse(models.Model):
    FUNCTIONAL = 'FUNCTIONAL'
    CLOSED = 'CLOSED'
    CHOICES = [
        (FUNCTIONAL, 'FUNCTIONAL'),
        (CLOSED, 'CLOSED'),
    ]

    warehouse_name = models.CharField(max_length=255)
    warehouse_description = models.TextField()
    warehouse_location = models.CharField(max_length=255)
    geofence_details = models.CharField(max_length=10000)
    status = models.CharField(
        max_length=50,
        choices=CHOICES,
        default=FUNCTIONAL,
    )

class Warehouse_deliveries(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_deliveries', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='warehouse_creator')
    scheduled_deliveries = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'warehouse_deliveries'
        ordering = ('-scheduled_deliveries',)

    def save(self, *args, **kwargs):
        super(Warehouse_deliveries, self).save(*args, **kwargs)        

class Warehouse_history(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_history', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='warehouse_creator1')
    history_deliveries = models.ForeignKey(Warehouse_deliveries, on_delete=models.CASCADE, related_name='history1')

    class Meta:
        verbose_name_plural = 'warehouse_history'
        ordering = ('-history_deliveries',)

class Warehouse_vehicles(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_vehicles', on_delete=models.CASCADE)
    assigned_vehicles = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'warehouse_vehicles'
        ordering = ('-assigned_vehicles',)