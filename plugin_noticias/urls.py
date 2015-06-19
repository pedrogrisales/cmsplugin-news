from django.conf.urls import patterns, include, url


import views



urlpatterns = patterns('',
	url(r'^archivo/(?P<slug>[-\w]+)/$', views.noticia_detalle, name="noticia_detalle"),
	url(r'^archivo/$', views.archivo, name="archivo"),
)
