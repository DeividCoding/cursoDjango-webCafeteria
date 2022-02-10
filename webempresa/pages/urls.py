from django.urls import path
from . import views

urlpatterns = [
    path('detailPage/<pk>/',views.DetailPage.as_view(),name='sample')
]