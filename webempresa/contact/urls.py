from django.urls import path
from . import views 

urlpatterns = [
    path('contact/',views.FormularioContacto.as_view(),name='contact'),
    path('exitoMensaje/',views.MensajeExito.as_view(),name="mensajeContactoExito")
]