# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Hotel,Customer,Reservation

#list all hotels view
def AllHotels(request):
    all_hotels="<h1><center> All Hotels </center></h1>"
    all_hotels +='<center><table border="solid 2px">'
    all_hotels+="<th> Name</th>"
    all_hotels+="<th> CIty</th>"
    all_hotels+="<th> Total_Rooms</th>"
    all_hotels+="<th> Empty_Rooms</th>"
    for hotel in Hotel.objects.all():
        all_hotels+="<tr>"
        all_hotels += "<td>" + hotel.hotel_name + "</td>"
        all_hotels +="<td>" + hotel.hotel_city + "</td>"
        all_hotels +="<td>" + str(hotel.all_rooms) + "</td>"
        all_hotels +="<td>" + str(hotel.empty_rooms) + "</td>"
        all_hotels+="</tr>"

    all_hotels += "</table></center>"
    return HttpResponse(all_hotels)



########list all customers view
def DisplayCustomers(request):
    all_customers="<h1><center> Customers </center></h1>"
    all_customers +='<center><table border="solid 2px">'
    all_customers+="<th> Name</th>"
    all_customers+="<th> Mobile</th>"
    for customer in Customer.objects.all():
        all_customers+="<tr>"
        all_customers += "<td>" + customer.customer_name + "</td>"
        all_customers +="<td>" + customer.customer_mobile + "</td>"
        all_customers+="</tr>"

    all_customers += "</table></center>"
    return HttpResponse(all_customers)


######list all reservation view
def DisplayReservation(request):
    all_reservation="<h1><center> Reservations </center></h1>"
    all_reservation +='<center><table border="solid 2px">'
    all_reservation+="<th> Customer Name</th>"
    all_reservation+="<th> Hotel Name</th>"
    all_reservation+="<th> From</th>"
    all_reservation+="<th> To</th>"
    for reserve in Reservation.objects.all():
        all_reservation+="<tr>"
        all_reservation += "<td>" +str(reserve.h_name)+ "</td>"
        all_reservation +="<td>" + str(reserve.c_name) + "</td>"
        all_reservation +="<td>" + str(reserve.start_time) + "</td>"
        all_reservation +="<td>" + str(reserve.end_time) + "</td>"
        all_reservation+="</tr>"
    all_reservation += "</table></center>"
    return HttpResponse(all_reservation)
