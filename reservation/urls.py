from django.conf.urls import url
from .views import AllHotels
from .views import DisplayCustomers
from .views import DisplayReservation

urlpatterns = [
    url(r"allhotels",AllHotels),
    url(r"displaycustomers",DisplayCustomers),
    url(r"reservationlist",DisplayReservation)

]