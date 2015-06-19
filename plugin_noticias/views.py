#encoding:utf-8

from datetime import datetime  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from models import NoticiaPluginModel

def archivo(request):
    data = {
        'noticias' : NoticiaPluginModel.objects.all()
    }         
    # paginator = Paginator(noticias_list, 3)
    # page = request.GET.get('page')
    # try:
    #     data['noticias'] = paginator.page(page)
    # except PageNotAnInteger:
    #     data['noticias'] = paginator.page(1)
    # except EmptyPage:
    #     data['noticias'] = paginator.page(paginator.num_pages)
    
    return render_to_response("plugin_noticias/archivo.html", data, context_instance=RequestContext(request))


def noticia_detalle(request, slug):
    data = {}
    data['instancia'] = get_object_or_404(NoticiaPluginModel,slug=slug)
    data['ultimas'] = NoticiaPluginModel.objects.filter(publicado=True, fecha_publicacion__lte=datetime.now).order_by('-fecha_publicacion')[:6]
    return render_to_response("plugin_noticias/detalle.html", data, context_instance=RequestContext(request))
    

