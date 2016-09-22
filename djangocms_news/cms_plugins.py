from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import NewsPluginModel, NewPluginModel
from datetime import datetime
import settings


class NewsPlugin(CMSPluginBase):
    model = NewsPluginModel
    name = _("Plugin News")
    render_template = NewsPluginModel.PLUGIN_TEMPLATES[0][0]


    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        olist = NewPluginModel.objects.filter(
            published=True
            #,date_publication__date__lte=datetime.now
        )#.order_by('-date_publication')

        context['thumbnail_size'] = settings.DJANGOCMS_NEWS_SETTINGS['THUMBNAIL_SIZE']        
        if instance.number:
            context['olist'] = olist[:instance.number]
        else:
            context['olist'] = olist
        return context



plugin_pool.register_plugin(NewsPlugin)
