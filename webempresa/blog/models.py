from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")

    # 'auto_now_add' añadira la hora a la cual se creado el modelo
    fechaCreacion=models.DateTimeField(auto_now_add=True)

    # 'auto_now' modificara la hora cada vez que se actualice la instancia
    fechaModificacion=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Post(models.Model):
    titulo=models.CharField(max_length=200,verbose_name="Titulo")
    contenido=RichTextUploadingField(verbose_name="Contenido")
    fechaPublicacion=models.DateTimeField(verbose_name="Fecha de la publicacion",default=now)
    imagen=models.ImageField("Image:",upload_to="imagenesDeBlog")

    # con 'on_delete' se le dice a django que debe hacer en caso de que
    # se elimine un 'User'  que pertenecia  a una o mas entradas
    # 1) 'models.CASCADE' ==> Lo que hara sera borrar todas las entradas
    # que pertenecen al usuario que teninan registrado como autor, es decir
    # si se eliminar un 'User' y ese 'User' era autor de una o mas entradas, entonces
    # dichas entradas seran eliminadas
    autor=models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)

    # Un 'Post' puede tener varias categorias, sin embargo eso tambien significa que una
    # categoria puede tener varios 'Post', es decir es posible que un 'Post' pertenesca a la
    # categoria 'Amor','Tecnologia','Drama', sin embargo tambien es posible que una la 'Category'
    # 'Amor' sea una cateogoria que pertenece al Post1, Post2 y Post9
    # Si quisieramos acceder a las categorias de un 'Post' en particular bastaria con poner:
    # 'nombrePost.categorias.all', pero... si quisieramos saber cuales son los 'Post' que 
    # incluyen una categoria en especifica ¿Como se haria? Bueno se hace uso del 'related_name'
    # es decir: 'nombreCategoria.nombreRelatedName.all' y listo!!!!!! para eso sirve el related_name 
    categorias=models.ManyToManyField(Category,verbose_name="Categorias",related_name='getPost')

    # 'auto_now_add' añadira la hora a la cual se creado el modelo
    fechaCreacion=models.DateTimeField(auto_now_add=True)

    # 'auto_now' modificara la hora cada vez que se actualice la instancia
    fechaModificacion=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

