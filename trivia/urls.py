from django.conf.urls import patterns, include, url

from .views import TriviaList


urlpatterns = patterns('',
    url(r'^$', TriviaList.as_view(), name='home'),
)
