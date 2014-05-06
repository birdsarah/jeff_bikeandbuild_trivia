from django.conf.urls import patterns, include, url

from .views import AboutView, SponsorsView, QuirksView


urlpatterns = patterns('',
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^sponsor/$', SponsorsView.as_view(), name='sponsor'),
    url(r'^quirks/$', QuirksView.as_view(), name='quirks'),
)
