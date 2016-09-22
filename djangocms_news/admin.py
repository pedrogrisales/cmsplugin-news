from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.forms import ModelForm
from djangocms_news.models import NewPluginModel

class MyModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class NewPluginModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    fieldsets = [
      ('Detail', {
        'classes': ('full-width',), 'fields': (
            'title',
            'detail',
            'date_publication',
            'published',
            'image'
        )
      }),
      ('Extra', {'classes': ('full-width',), 'fields': ('slug',)}),
    ]

    date_hierarchy = 'date_publication'
    list_display = ('date_publication','title',  'published')
    list_display_links = ('title',)
    list_filter = ('title', )

admin.site.register(NewPluginModel, NewPluginModelAdmin)
