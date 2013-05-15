from django.conf.urls import patterns, include, url

from igratacels.views import *

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from igratacels.models import *
from igratacels.forms import EstilForm, MaterialForm, ArquitecteForm, GratacelForm
from igratacels.views import MaterialCreate, EstilCreate, ArquitecteCreate, GratacelCreate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gratacels.views.home', name='home'),
    # url(r'^gratacels/', include('gratacels.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^materials/create/$', MaterialCreate.as_view(), name='material_create'),
    url(r'^estils/create/$', EstilCreate.as_view(), name='estil_create'),
    url(r'^arquitectes/create/$', ArquitecteCreate.as_view(), name='arquitecte_create'),
    url(r'^gratacels/create/$', GratacelCreate.as_view(), name='gratacel_create'),

    url(r'^material/(?P<pk>\d+)/edit/$',
	 UpdateView.as_view(model = Material, 
	 template_name = 'form.html',
	 form_class = MaterialForm),
	 name='material_edit'),
    url(r'^estil/(?P<pk>\d+)/edit/$',
	 UpdateView.as_view(model = Estil, 
	 template_name = 'form.html',
	 form_class = EstilForm),
	 name='estil_edit'),
    url(r'^arquitecte/(?P<pk>\d+)/edit/$',
	 UpdateView.as_view(model = Arquitecte, 
	 template_name = 'form.html',
	 form_class = ArquitecteForm),
	 name='arquitecte_edit'),
    url(r'^gratacel/(?P<pk>\d+)/edit/$',
	 UpdateView.as_view(model = Gratacel, 
	 template_name = 'form.html',
	 form_class = GratacelForm), 
	 name='gratacel_edit'),
	
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    url(r'^home', mainpage, name='home'),
    url(r'^gratacel/(\w+)$', gratacelpage),
    url(r'^gratacels/', gratacel_list),
    url(r'^arquitecte/(\w+)', arquitectepage),
    url(r'^arquitectes/$', 'igratacels.views.arquitecte_list'),
    url(r'^estil/(\w+)$', estilpage),
    url(r'^estils/$', 'igratacels.views.estil_list'),
    url(r'material/(\w+)/$', materialpage),
    url(r'materials/$', 'igratacels.views.material_list'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$', 'django.contrib.auth.views.login'),
)
