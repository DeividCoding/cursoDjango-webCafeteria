from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('fechaCreacion','fechaModificacion')

admin.site.register(Service,ServiceAdmin)
