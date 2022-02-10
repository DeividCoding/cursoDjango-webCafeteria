from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import FormularioContacto
from django.urls import reverse_lazy
from django.core.mail import send_mail
from webempresa.settings import EMAIL_HOST_USER

# Create your views here.
class MensajeExito(TemplateView):
    template_name="contact/exitoRegistro.html"


class FormularioContacto(FormView):
    template_name='contact/contact.html'
    form_class=FormularioContacto
    success_url=reverse_lazy('mensajeContactoExito')
    #success_url="contact/exitoRegistro.html"

    def form_valid(self,form):
        nombre=self.request.POST.get('name')
        correo=self.request.POST.get('email')
        contenido=self.request.POST.get('content')

        # mensaje para el usuario 
        asunto="Recepccion exitosa de mensaje de WEB  cafeteria"
        mensaje="Hola {}, hemos recibido exitosamente tu mensaje "\
            "gracias por contactarte con nosotros".format(nombre)
        email_remitente=EMAIL_HOST_USER        
        # debe ser una lista por que se espera que el email de destino
        # pueda ser desde 1 email, hasta n emails.
        email_destino=[correo,]
        send_mail(asunto,mensaje,email_remitente,email_destino)

        # mensaje para el programador
        asunto="WEB cafeteria, mensaje de cliente"
        mensaje="** Nombre de cliente:\n{}\n**Correo de cliente:\n{}\n**Mensaje:\n\t{}".format(nombre,correo,contenido)
        email_destino=[EMAIL_HOST_USER]
        send_mail(asunto,mensaje,email_remitente,email_destino)

        return super(FormularioContacto,self).form_valid(form)
