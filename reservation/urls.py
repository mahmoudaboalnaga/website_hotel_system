from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"allhotels",AllHotels),
    url(r"displaycustomers",DisplayCustomers),
    url(r"reservationlist",DisplayReservation)

]