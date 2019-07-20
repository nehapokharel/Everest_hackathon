# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Client

# Register your models here.

@admin.register(Client)
class ClientAdmin(OSMGeoAdmin):
    list_display = ('full_name', 'location')