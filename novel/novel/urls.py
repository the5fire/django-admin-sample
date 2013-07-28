#coding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

#import xadmin
#xadmin.autodiscover()

from django.contrib import admin
admin.autodiscover()

import djadmin2
djadmin2.default.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'book.views.index', name='index'),
    #url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^admin2/', include(djadmin2.default.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
