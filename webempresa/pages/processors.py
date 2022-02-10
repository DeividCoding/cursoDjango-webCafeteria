from .models import Page

def get_pages_footer(request):
    paginas=( (cadaPagina.id,cadaPagina.titulo) for cadaPagina in Page.objects.all() )
    return {
        'PAGINAS_FOOTER':paginas
    }
