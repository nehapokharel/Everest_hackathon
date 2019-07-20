# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Client Model

class Client(models.Model):
    full_name = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=500)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(
        upload_to='team/admin/', blank=True, null=True)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


class Ambulance(models.Model):

    Organization_Name = models.CharField(max_length=500)
