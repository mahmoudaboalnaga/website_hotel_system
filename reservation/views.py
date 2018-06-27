# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Hotel,Customer,Reservation

#list all hotels view
def AllHotels(request):
 
    return render(request,"reservation/hotel.html",
                    {'hotel':Hotel.objects.all()}
                 )



########list all customers view
def DisplayCustomers(request):
    return render(request,"reservation/customer.html",
                    {'customer':Customer.objects.all()}    
    )


######list all reservation view
def DisplayReservation(request):
    return render(request,"reservation/reservations.html",
        {'reservation':Reservation.objects.all()}
    )

