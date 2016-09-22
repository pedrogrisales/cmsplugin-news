#encoding:utf-8
from __future__ import unicode_literals

from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from models import NewPluginModel

def news(request):
    data = {
        'news' : NewPluginModel.objects.all()
    }
    return render_to_response("djangocms_news/news.html", data, context_instance=RequestContext(request))


def news_detail(request, slug):
    data = {}
    data['instance'] = get_object_or_404(NewPluginModel,slug=slug)
    data['lates'] = NewPluginModel.objects.all()[:6]#filter(published=True, date_publication__lte=datetime.now).order_by('-date_publication')
    return render_to_response("djangocms_news/detail.html", data, context_instance=RequestContext(request))
