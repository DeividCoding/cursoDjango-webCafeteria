from .models import Link

def contexto_contactos(request):
    redesSociales=dict( ("CONTACTO_"+str(redSocial),redSocial.url) for redSocial in Link.objects.all() )
    print("*"*100)
    print(redesSociales)
    return redesSociales
    