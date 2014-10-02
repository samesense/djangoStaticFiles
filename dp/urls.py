from django.conf.urls import patterns, url

from dp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
