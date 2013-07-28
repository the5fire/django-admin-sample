from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import djadmin2
djadmin2.default.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'novel.views.home', name='home'),
    # url(r'^novel/', include('novel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin2/', include(djadmin2.default.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
