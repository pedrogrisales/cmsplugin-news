from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import NoticiasPluginModel, NoticiaPluginModel
from datetime import datetime


class NoticiasPlugin(CMSPluginBase):    
    model = NoticiasPluginModel
    name = _("Plugin Noticias")
    render_template = NoticiasPluginModel.PLUGIN_TEMPLATES[0][0]
    

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template
        
        
        lista = NoticiaPluginModel.objects.filter(publicado=True, fecha_publicacion__lte=datetime.now).order_by('-fecha_publicacion')
        
        context['columns'] = str(12/instance.columns)
        if instance.numero:
            context['lista'] = lista[:instance.numero]
        else:
            context['lista'] = lista    
        return context



plugin_pool.register_plugin(NoticiasPlugin)
