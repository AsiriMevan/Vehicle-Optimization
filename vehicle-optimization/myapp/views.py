from operator import ge
from django.forms import forms
from django.http import request
from django.shortcuts import redirect, render
from django.template import context
from wialon.api import Wialon, WialonError
from wialon import flags
import json
from .models import Client
from .forms import CreateClient
from .models import Vehicle
from .forms import createVehicle

# Create your views here.
def index(request):
    return render(request, 'index.html')

def checkpoint(request):
    return render(request, 'checkpoint.html')

# View Function of the Vehicle Model
#Start

def vehicleModule(request):
    context = {}
    form = createVehicle(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicleView')

    context['form']= form
    return render(request, 'vehicle.html', context)

def vehicleviewpage(request):
    vehicles = Vehicle.objects.all()
    data = {
        'vehicles': vehicles
    }
    return render(request, 'vehicleView.html',data)

def vehicleUpdate(request, pk):
    vehicles = Vehicle.objects.get(vehicle_Id=pk)
    form = createVehicle(instance=vehicles)

    if request.method == 'POST':
        form = createVehicle(request.POST, instance=vehicles)
        if form.is_valid():
            form.save()
            return redirect('vehicleView')
            
    context = {'form':form}
    return render(request, 'vehicle.html', context)

def vehicleDelete(request, pk):

    vehicles = Vehicle.objects.get(vehicle_Id=pk)
    if request.method == "POST":
        vehicles.delete()
        return redirect('vehicleView')
        
    context = {'item':vehicles}
    return render(request, 'vehicleDelete.html', context)

#End

def checkpointdetails(request):
    try:
        token = '0309e293ca53c711623c73793c41f70624EB61F1D32399BFC0222FCF0CA5B58E538234BA'
        wialon_api = Wialon()
        result = wialon_api.token_login(token=token)
        wialon_api.sid = result['eid']

    # search for resources to find resource id
        params = {
            "spec": {
                "itemsType": 'avl_resource',
                "propName": 'sys_name',
                "propValueMask": '*',
                "sortType": 'sys_name',
            },
                "flags": 0x3FFFFFFFFFFFFFFF,
                "force": 1,
                "from": 0,
                "to": 0
            }
        result = wialon_api.core_search_items(params)
        warehouseID = result['items'][1]['zg']['1']['zns']
        warehouseID = [str(i) for i in warehouseID]
        clientID = result['items'][1]['zg']['2']['zns']
        clientID = [str(i) for i in clientID]
        geofences = result['items'][1]['zl']

        loc_id = list(geofences.keys())
        w_info = []
        c_info = []
        for i in loc_id:
            if i in warehouseID:
                w_info.append(geofences[i])
            if i in clientID:
                c_info.append(geofences[i])        
        print(w_info)
    except WialonError as e:
        print(e)
       
    a = json.dumps(c_info)
    b = json.dumps(w_info)
    wialon_api.core_logout()
    return render(request, 'checkpointdetails.html', {'warehouse': b, 'client': a})

def clientCreation(reqeust):
    if request.method == 'POST':
        if request.POST.get('client_name') and request.POST.get('client_description') and reqeust.POST.get('email') and request.POST.get('contact_number') and request.POST.get('address') and request.POST.get('client_priority') and reqeust.POST.get('geofence_details'):
            client = Client()
            client.client_name = reqeust.POST.get('client_name')
            client.client_description = reqeust.POST.get('client_description')
            client.email = reqeust.POST.get('email')
            client.contact_number = reqeust.POST.get('contact_number')
            client.address = request.POST.get('address')
            client.client_priority = reqeust.POST.get('client_priority')
            client.geofence_details = request.POST.get('geofence_details')
            client.save()

            return render(reqeust, 'clientCreation.html')
        else:
            return render(request, 'clientCreation.html')


