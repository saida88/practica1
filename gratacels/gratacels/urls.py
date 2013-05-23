from django.conf.urls import patterns, include, url

from igratacels.views import *

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from igratacels.models import *
from igratacels.forms import EstilForm, MaterialForm, ArquitecteForm, GratacelForm
from igratacels.views import MaterialCreate, EstilCreate, ArquitecteCreate, GratacelCreate
from igratacels.views import APIGratacelList, APIGratacelDetail, APIEstilList, APIEstilDetail, \
			     APIMaterialList, APIMaterialDetail, APIArquitecteList, APIArquitecteDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gratacels.views.home', name='home'),
    # url(r'^gratacels/', include('gratacels.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#OTHER URL
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', mainpage, name='home'),
    url(r'^home', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

#CREATE URL
    url(r'^materials/create/$',
	MaterialCreate.as_view(),
	name='material_create'),
    url(r'^estils/create/$',
	EstilCreate.as_view(),
	name='estil_create'),
    url(r'^arquitectes/create/$',
	ArquitecteCreate.as_view(),
	name='arquitecte_create'),
    url(r'^gratacels/create/$',
	GratacelCreate.as_view(),
	name='gratacel_create'),

#EDIT URL
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

#LIST URL
    url(r'^gratacels/', gratacel_list,
	name='gratacel_list'),
    url(r'^arquitectes/$', 'igratacels.views.arquitecte_list',
	name='arquitecte_list'),
    url(r'^estils/$', 'igratacels.views.estil_list',
	name='estil_list'),
    url(r'^materials/$', 'igratacels.views.material_list',
	name='material_list'),

#DETAIL URL	
    url(r'^gratacel/(?P<idGratacel>\d+)$',
	'igratacels.views.gratacelpage',
	name='gratacel_detail'),
    url(r'^arquitecte/(?P<idArquitecte>\d+)$',
	'igratacels.views.arquitectepage',
	name='arquitecte_detail'),
    url(r'^estil/(?P<idEstil>\d+)$',
	'igratacels.views.estilpage',
	name='estil_detail'),
    url(r'^material/(?P<idMaterial>\d+)/$',
	'igratacels.views.materialpage',
	name='material_detail'),



#DELETE URL	
    url(r'^gratacel/(?P<pk>\d+)/delete/$',
	GratacelDelete.as_view(),
	name='gratacel_delete'),
    url(r'^arquitecte/(?P<pk>\d+)/delete/$',
	ArquitecteDelete.as_view(),
	name='arquitecte_delete'),
    url(r'^estil/(?P<pk>\d+)/delete/$',
	EstilDelete.as_view(),
	name='estil_delete'),
    url(r'^material/(?P<pk>\d+)/delete/$',
	MaterialDelete.as_view(),
	name='material_delete'),




#API URL
url(r'^api/gratacel/$', APIGratacelList.as_view(), name='gratacel-list'),
url(r'^api/gratacel/(?P<pk>\d+)/$', APIGratacelDetail.as_view(), name='gratacel-detail'),
url(r'^api/material/$', APIMaterialList.as_view(), name='material-list'),
url(r'^api/material/(?P<pk>\d+)/$', APIMaterialDetail.as_view(), name='material-detail'),
url(r'^api/estil/$', APIEstilList.as_view(), name='estil-list'),
url(r'^api/estil/(?P<pk>\d+)/$', APIEstilDetail.as_view(), name='estil-detail'),
url(r'^api/arquitecte/$', APIArquitecteList.as_view(), name='arquitecte-list'),
url(r'^api/arquitecte/(?P<pk>\d+)/$', APIArquitecteDetail.as_view(), name='arquitecte-detail'),

)
