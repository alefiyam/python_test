# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.get_que_ans, name='get_que_ans'),
    url(r'^get_que_by_search_term/$', views.get_que_by_search_term, name='get_que_by_search_term')
]
