from django.contrib import admin
from django.db import models
from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields=("created","modified")
    
admin.site.register(Link,LinkAdmin)