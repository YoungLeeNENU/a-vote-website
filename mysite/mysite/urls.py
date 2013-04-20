# -*- coding:utf-8 -*-
## 当前 Django 的 URL 规则声明
## 是一个内容清单
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^polls/', include('polls.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
