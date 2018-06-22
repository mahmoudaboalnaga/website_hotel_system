# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hotel,Customer,Reservation

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Reservation)
