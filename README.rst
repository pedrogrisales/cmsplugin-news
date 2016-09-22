=====
cmsplugin-news
=====

djangocms_news is a plugin for django-cms

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "djangocms_news" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'djangocms_news',
    )

2. Include the djangocms_news URLconf in your project urls.py like this::

    url(r'^', include('djangocms_news.urls')),

3. Run `python manage.py migrate djangocms_news` to create the djangocms_news models.
