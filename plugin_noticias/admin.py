from django.contrib import admin
from django.utils.translation import ugettext as _
from cms.admin.placeholderadmin import PlaceholderAdmin
from django.forms import ModelForm


from models import NoticiaPluginModel


from cms.forms.widgets import PluginEditor


class NoticiaAdmin(PlaceholderAdmin):
    fieldsets = [
      ('Datos', {'classes': ('full-width',), 'fields': ('titulo', 'fecha_publicacion', 'publicado')}),
      ('Detalle', {'classes': ('full-width',), 'fields': ('detalle',)}),
      ('Imagen', {'classes': ('full-width',), 'fields': ('imagen',)})

    ]

    date_hierarchy = 'fecha_publicacion'
    list_display = ('fecha_publicacion','titulo',  'publicado')
    list_display_links = ('titulo',)
    list_filter = ('titulo', )


    class Media:
        js = ( 'js/jquery.min.js',)

admin.site.register(NoticiaPluginModel, NoticiaAdmin)


