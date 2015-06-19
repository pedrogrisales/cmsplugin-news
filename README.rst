=====
cmsplugin-news
=====

plugin_noticias is a plugin for django-cms

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "plugin_noticias" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'plugin_noticias',
    )

2. Include the plugin_noticias URLconf in your project urls.py like this::

    url(r'^', include('plugin_noticias.urls')),

3. Run `python manage.py migrate plugin_noticias` to create the plugin_noticias models.

