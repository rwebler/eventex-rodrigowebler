#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'eventex.core.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', 'speaker_detail', name='speaker_detail'),
    url(r'^palestras/$', 'talk_list', name='talk_list'),
    url(r'^palestras/(?P<pk>\d+)/$', 'talk_detail', name='talk_detail'),
)
