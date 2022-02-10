from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class About(TemplateView):
    template_name="Core/about.html"

class Index(TemplateView):
    template_name="Core/index.html"

class Sample(TemplateView):
    template_name="Core/sample.html"

class Services(TemplateView):
    template_name="Core/services.html"

class Store(TemplateView):
    template_name="Core/store.html"




