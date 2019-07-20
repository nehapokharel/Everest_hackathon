from __future__ import unicode_literals
from django.shortcuts import render
import django.contrib
from sewa import views
from django.views.generic import TemplateView


class UserView(TemplateView):
    template_name = 'clienttemplates/home.html'


# class UserLocationAccessView(ListView):
# 	model = User

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['userlocation'] = User.objects.all()
#         if geolocation in userlocation:
#         	pass
#         else:
#         	pass 

