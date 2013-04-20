# -*- coding:utf-8 -*-
## 当前 Django 的 URL 规则声明
## 是一个内容清单
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.contrib import admin
from polls.models import Poll
    
admin.autodiscover()

'''
# 投票视图
urlpatterns = patterns('polls.views',
                       url(r'^$',                          'index'),
                       url(r'^(?P<poll_id>\d+)/$',         'detail'),
                       url(r'^(?P<poll_id>\d+)/results/$', 'results'),
                       url(r'^(?P<poll_id>\d+)/vote/$',    'vote'),
)
'''

# 投票视图
urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(
                               queryset = Poll.objects.order_by('-pub_date')[:5],
                               context_object_name = 'latest_poll_list',
                               template_name = 'polls/index.html')),
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(
                               model = Poll,
                               template_name = 'polls/detail.html')),
                       url(r'^(?P<pk>\d+)/results/$',
                           DetailView.as_view(
                               model = Poll,
                               template_name = 'polls/results.html'),
                           name = 'poll_results'),
                       url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)

# admin视图
urlpatterns += patterns('',
                        url(r'^admin/', include(admin.site.urls)),
)
