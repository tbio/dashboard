# -*- coding: utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns(
    'www.views',
    url(r'^$', 'stream', name='stream'),
)
