from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from sewa.views import *


app_name = "sewa"
urlpatterns = [
    path('', UserView.as_view(), name='userhome'),
]
