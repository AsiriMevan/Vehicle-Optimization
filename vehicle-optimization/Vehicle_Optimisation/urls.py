"""Vehicle_Optimisation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('checkpoint', views.checkpoint, name='checkpoint'),
    path('checkpointdetails', views.checkpointdetails, name='checkpointdetails'),
    path('clientCreation', views.clientCreation, name='clientCreation'),

# Url Function of the Vehicle Model
#Start
    path('vehicleModule',views.vehicleModule,name='vehicleModule'),
    path('vehicleView', views.vehicleviewpage, name='vehicleView'),
    path('vehicleUpdate/<str:pk>/',views.vehicleUpdate,name='vehicleUpdate'),
    path('vehicleDelete/<str:pk>/',views.vehicleDelete,name='vehicleDelete'),
#End
]
