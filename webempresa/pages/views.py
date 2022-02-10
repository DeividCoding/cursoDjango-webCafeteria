from django.shortcuts import render
from django.views.generic import DetailView
from .models import Page
# Create your views here.


class DetailPage(DetailView):
    model=Page
    template_name='pages/sample.html'
