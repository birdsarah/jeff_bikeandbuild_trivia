from django.conf.urls import patterns, include, url

from .views import TriviaList, TriviaCheckout


urlpatterns = patterns('',
    url(r'^$', TriviaList.as_view(), name='home'),
    url(r'^send$', TriviaCheckout.as_view(), name='send'),
)
