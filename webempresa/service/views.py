from django.shortcuts import render
from django.views.generic import ListView
from .models import Service
# Create your views here.


class Services(ListView):
    template_name="service/services.html"
    context_object_name="listaServicios"
    model=Service


