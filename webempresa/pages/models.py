from django.db import models

# Create your models here.

from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from model_utils.models import TimeStampedModel
# Create your models here.
class Page(TimeStampedModel):
    titulo=models.CharField(verbose_name="Titulo",max_length=200)
    content=models.TextField(verbose_name="Contenido")
    orden=models.SmallIntegerField(verbose_name="Orden",default=0)

    class Meta:
        verbose_name="pagina"
        verbose_name_plural="paginas"
        ordering=['orden','titulo']


    def __str__(self):
        return self.titulo

