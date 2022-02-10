from django.db import models

# Create your models here.

class Service(models.Model):
    
    imagen=models.ImageField(verbose_name="Imagen del servicio:",upload_to="imagenesServicios")
    titulo=models.CharField(max_length=200,verbose_name="Titulo:")
    subtitulo=models.CharField(max_length=200,verbose_name="Subtitulo:")
    contenido=models.TextField(verbose_name="Contenido del servicio:")
    
    
    # 'auto_now_add' añadira la hora a la cual se creado el modelo
    fechaCreacion=models.DateTimeField(auto_now_add=True)

    # 'auto_now' modificara la hora cada vez que se actualice la instancia
    fechaModificacion=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"

        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['-fechaCreacion']

    def __str__(self):
        return self.titulo

