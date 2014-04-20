from django.conf.urls import patterns, include, url

from .views import TriviaList, TriviaCheckout, AddGuesses


urlpatterns = patterns('',
    url(r'^$', TriviaList.as_view(), name='home'),
    url(r'^trivia/(?P<pk>\d+)/$', AddGuesses.as_view(), name='trivia_detail'),
    url(r'^send$', TriviaCheckout.as_view(), name='send'),
)
