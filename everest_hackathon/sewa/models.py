# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Client Model


class Location(models.Model):
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


class Client(Location):

    full_name = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(
        upload_to='team/admin/', blank=True, null=True)


class Ambulance(Location):

    Organization_Name = models.CharField(max_length=500)
