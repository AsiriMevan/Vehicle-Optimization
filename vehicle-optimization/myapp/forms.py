from django import forms
from .models import Client
from .models import Vehicle
from django.db import transaction

class CreateClient(forms.Form):
    client_name = forms.CharField(required=True)
    client_description = forms.CharField()
    email = forms.EmailField(required=True)
    contact_number = forms.CharField(required=True)
    address = forms.CharField()
    client_priority = forms.CharField()
    geofence_details = forms.CharField(required=True)

    # class Meta(forms.Meta):
    #     model = Client

    # @transaction.atomic
    # def save(self):
    #     client = super().save(commit=False)
    #     client.is_admin = True
    #     client.first_name = self.cleaned_data.get('first_name')
    #     client.last_name = self.cleaned_data.get('last_name')
    #     client.email=self.cleaned_data.get('email')
    #     client.save()
    #     admin = Admin.objects.create(user=user)
    #     admin.phone_number=self.cleaned_data.get('phone_number')
       
    #     admin.save()
    #     return user


class createVehicle(forms.ModelForm):

    class Meta:
        model = Vehicle

        fields = [
            "vehicle_Id",
            "vehicle_Brand",
            "vehicle_Number",
            "vehicle_Type",
            "scheduled_Date",
            "scheduled_Location",
            "designated_Driver",
            "warehouse",
            "capacity",
            "status",
        ]

    # vehicle_Id = forms.CharField(required=True)
    # vehicle_Brand = forms.CharField(required=True)
    # vehicle_Number = forms.CharField(required=True)
    # vehicle_Type = forms.CharField(required=True)
    # scheduled_Date = forms.DateField()
    # scheduled_Location = forms.CharField(required=True)
    # designated_Driver = forms.CharField(required=True)
    # warehouse = forms.CharField(required=True)
    # capacity = forms.CharField(required=True)
    # status = forms.CharField(required=True)