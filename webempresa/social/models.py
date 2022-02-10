from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from model_utils.models import TimeStampedModel
# Create your models here.
class Link(TimeStampedModel):
    # REDES SOCIALES
    FACEBOOK_RED_SOCIAL='1'
    YOUTUBE_RED_SOCIAL='2'
    INSTAGRAM_RED_SOCIAL='3'
    LINKEDIN_RED_SOCIAL='4'
    TWITTER_RED_SOCIAL='5'

    REDES_SOCIALES={
        FACEBOOK_RED_SOCIAL:"Facebook",
        YOUTUBE_RED_SOCIAL:"Youtube",
        INSTAGRAM_RED_SOCIAL:"Instragram",
        LINKEDIN_RED_SOCIAL:"LinkedIn",
        TWITTER_RED_SOCIAL:"Twitter"
    }

    nombreRedSocial=models.CharField(
        verbose_name="Red social",
        max_length=1,
        choices=tuple(REDES_SOCIALES.items()),
        unique=True
    )
    url=models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
    
    class Meta:
        verbose_name="Enlace"
        verbose_name_plural="Enlaces"
        ordering=['nombreRedSocial']
    
    def __str__(self):
        return "{}".format( self.REDES_SOCIALES[self.nombreRedSocial]  )


        
