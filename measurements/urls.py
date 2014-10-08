# -*- coding: utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns(
    'measurements.views',
    url(r'^idealrate/$', 'idrate', name='idrate'),
    url(r'^maxrate/$', 'maxrate', name='maxrate'),
    url(r'^recovery/$', 'recovery', name='recovery'),
)
