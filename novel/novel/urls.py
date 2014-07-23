#coding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

# 开启 xadmin之后django自带的admin不可用
import xadmin
xadmin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'book.views.index', name='index'),
    url(r'^xadmin/', include(xadmin.site.urls)),
)
