from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.About.as_view(),name='about'),
    path('store/',views.Store.as_view(),name='store'),

]