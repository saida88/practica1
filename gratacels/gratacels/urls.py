from django.conf.urls import patterns, include, url

from igratacels.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gratacels.views.home', name='home'),
    # url(r'^gratacels/', include('gratacels.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    url(r'^home', mainpage, name='home'),
    url(r'^gratacel/(\w+)$', gratacelpage),
    url(r'^gratacel/', gratacel_list),
    url(r'^arquitecte/(\w+)', arquitectepage),
    url(r'^arquitecte/$', 'igratacels.views.arquitecte_list'),
    url(r'^estil/(\w+)$', estilpage),
    url(r'^estil/$', 'igratacels.views.estil_list'),
    url(r'material/(\w+)/$', materialpage),
    url(r'material/$', 'igratacels.views.material_list'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$', 'django.contrib.auth.views.login'),


   
)
