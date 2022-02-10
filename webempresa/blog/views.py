from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Category, Post
from django.http import Http404




# Create your views here.
class BlogListView(ListView):
    template_name="blog/blog.html"
    context_object_name="listaPublicaciones"


    def get_queryset(self):
        idCategoria=self.request.GET.get( 'idCategoria','' )
        if idCategoria:
            try:
                unaCategoria=get_object_or_404(Category,id=idCategoria)
            except Category.DoesNotExist:
                raise Http404("No existe ninguna categoria con id=",idCategoria)
            listaPublicaciones=unaCategoria.getPost.all
        else:
            listaPublicaciones=Post.objects.all()

        return listaPublicaciones





