from django.conf.urls import url
from .views import AllHotels

urlpatterns = [
    url(r"allhotels",AllHotels)
    
]