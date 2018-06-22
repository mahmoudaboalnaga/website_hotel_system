# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_city=models.CharField(max_length=100)
    all_rooms=models.IntegerField()
    empty_rooms=models.IntegerField()


    def __str__(self):
        return self.hotel_name


class Customer(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Reservation(models.Model):
    h_name=models.ForeignKey(Hotel)
    c_name=models.ForeignKey(Customer)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()


    def __str__(self):
        return self.h_name.hotel_name +"for "+self.c_name.customer_name
                 
