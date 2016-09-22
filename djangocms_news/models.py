from __future__ import unicode_literals

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.db.models import permalink
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField
from django.template.defaultfilters import slugify
from djangocms_text_ckeditor.fields import HTMLField

class NewsPluginModel(CMSPlugin):
    PLUGIN_TEMPLATES = (
        # ('plugin_noticias/barra.html', 'Barra'),
        # ('plugin_noticias/lista.html', 'Lista'),
        ('djangocms_news/mosaic.html', 'Mosaico'),
    )
    number = models.IntegerField(default=0)
    template = models.CharField('Template', max_length=255,
                                choices = PLUGIN_TEMPLATES)


class NewPluginModel(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_publication = models.DateField(blank=False)
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=250,blank=False)
    slug = models.SlugField(max_length=250,blank=True,unique=True)
    image = FilerImageField(blank=False, null=True)
    detail = HTMLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewPluginModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('news_detail', None, { 'slug': self.slug.lower() })

    class Meta:
        ordering = ('-date_publication',)
        verbose_name = 'New'
        verbose_name_plural = 'News'
