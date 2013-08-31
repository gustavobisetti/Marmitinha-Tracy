from django.conf.urls import patterns, include, url

from .views import CheckPersonView, UncheckPersonView


urlpatterns = patterns('',
    url(r'^check/$', CheckPersonView.as_view(), name='check_person'),
    url(r'^uncheck/$', UncheckPersonView.as_view(), name='uncheck_person'),
)