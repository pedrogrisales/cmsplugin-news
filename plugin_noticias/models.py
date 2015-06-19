from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.db.models import permalink
from filer.fields.image import FilerImageField
from cms.models.fields import PlaceholderField
from django.template.defaultfilters import slugify

class NoticiasPluginModel(CMSPlugin):
    PLUGIN_TEMPLATES = (
        # ('plugin_noticias/barra.html', 'Barra'),
        # ('plugin_noticias/lista.html', 'Lista'),
        ('plugin_noticias/mosaico.html', 'Mosaico'),
    )
    PLUGIN_COLUMNS = (
        (2, "Dos columnas"),
        (3, "Tres columnas"),
    )

    numero = models.IntegerField(default=0)
    template = models.CharField('Template', max_length=255,
                                choices = PLUGIN_TEMPLATES)
    columns = models.IntegerField(choices=PLUGIN_COLUMNS, default=1)


class NoticiaPluginModel(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_publicacion = models.DateField(blank=False)
    publicado = models.BooleanField(default=False)
    titulo = models.CharField(max_length=250,blank=False)
    slug = models.SlugField(max_length=250,blank=True,unique=True)
    imagen = FilerImageField(blank=False, null=True)
    detalle = PlaceholderField('detalle')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(NoticiaPluginModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.titulo

    @permalink
    def get_absolute_url(self):
        return ('noticia_detalle', None, { 'slug': self.slug.lower() })

    class Meta:
        ordering = ('-fecha_publicacion',)
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
