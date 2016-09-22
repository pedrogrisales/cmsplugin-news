from django.conf import settings

DJANGOCMS_NEWS_SETTINGS = getattr(settings, 'DJANGOCMS_NEWS_SETTINGS', {
    'THUMBNAIL_SIZE' : '270x160'
})
