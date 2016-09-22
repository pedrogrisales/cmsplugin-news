from __future__ import unicode_literals

import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^news/(?P<slug>[-\w]+)/$', views.news_detail, name="news_detail"),
	url(r'^news/$', views.news, name="news"),
)
