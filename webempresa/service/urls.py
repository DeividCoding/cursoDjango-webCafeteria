from django.urls import path
from . import views

urlpatterns = [
    path('services/',views.Services.as_view(),name='services'),
]