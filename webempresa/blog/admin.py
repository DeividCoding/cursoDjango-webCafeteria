from django.contrib import admin
from .models import Category,Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields=(
        'fechaCreacion',
        'fechaModificacion'
        )


    # los datos que se mostraran de cada instancia del modelo 'Post'
    list_display=('titulo','autor','Categorias' )

    # Las instancias de modelo 'Post' sera ordenadas por 'autor' y 
    # 'fecha de publicacion'
    ordering=('autor','fechaPublicacion')

    # El buscados de instancias del modelo 'Post' buscara dichas instancias
    # por 'titulo' o por 'nombre del autor'
    search_fields=('titulo','autor__username')


    # Cuando se trabajando con modelos que tienen apartados de 'DateTime' se
    # puede usar una 'JERARQUIA DE FECHA', es decir en el encabezado del administrador
    # habra un menu el cual tendra diferentes fechas, y cada vez que el usuario de 
    # clic sobre uno de ellos, se le mostraran las instancias que esten en ese rango
    # de fechas, a continuacion se hara una jerarquia por fechas del apartado 'fechaPublicacion'
    date_hierarchy='fechaPublicacion'

    # Los filtros que se pondran
    list_filter=('autor__username','categorias__name')

    def Categorias(self,objeto):
        '''
        Valor que tendra cada objeto en la columna 'Categorias' 
        '''
        return ",".join( (cadaCategoria.name  for cadaCategoria in objeto.categorias.all() )  )


admin.site.register(Category)
admin.site.register(Post,PostAdmin)






