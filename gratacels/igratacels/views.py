# Create your views here.

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from igratacels.models import *
from forms import *
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from serializers import ArquitecteSerializer, EstilSerializer, MaterialSerializer, GratacelSerializer



def mainpage(request):
	return render_to_response(
		'mainpage.html',
		{
			'titlehead': 'Gratacels aPP',
			'pagetitle': 'Welcome to the Gratacels aPPlication',
			'contentbody': 'Managing non legal funding since 2013',
			'user': request.user

		})
	output = template.render(variables)
	return HttpResponse(output)

def gratacelpage(request, idGratacel):

	try:
		gratacel = Gratacel.objects.get(idGratacel=idGratacel)
	except:
		raise Http404('Gratacel no trobat')

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('gratacelpage.xml')
	elif parametre =="JSON":
		template = get_template('gratacelpage.js')	
	else:
		template = get_template('gratacelpage.html')
	arquitectes = gratacel.arquitectes.all()
	materials = gratacel.materials.all()
	estils = Estil.objects.get(idEstil=gratacel.idEstil_id)
	variables = Context({
		'gratacel': gratacel,
		'arquitectes': arquitectes,
		'estils': estils,
		'materials': materials,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def gratacel_list(request):
	try:
		gratacels = Gratacel.objects.all()
	except:
		raise Http404('Materials no trobats')

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('gratacel_list.xml')
	elif parametre =="JSON":
		template = get_template('gratacel_list.js')	
	else:
		template = get_template('gratacel_list.html')

	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'gratacels': gratacels,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def arquitectepage(request, idArquitecte):

	try:
		arquitecte = Arquitecte.objects.get(idArquitecte=idArquitecte)
	except:
		raise Http404('Arquitecte no trobat')

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('arquitectepage.xml')
	elif parametre =="JSON":
		template = get_template('arquitectepage.js')	
	else:
		template = get_template('arquitectepage.html')

	gratacels=arquitecte.gratacel_set.all()
	variables = Context({
		'arquitecte': arquitecte,
		'gratacels': gratacels,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def estilpage(request, idEstil):

	try:
		estil = Estil.objects.get(idEstil=idEstil)
	except:
		raise Http404('Estil no trobat')
	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('estilpage.xml')
	elif parametre =="JSON":
		template = get_template('estilpage.js')	
	else:
		template = get_template('estilpage.html')

	gratacels=estil.gratacel_set.all()	
	variables = Context({
		'estil': estil,
		'gratacels': gratacels,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def materialpage(request, idMaterial):

	try:
		material = Material.objects.get(idMaterial=idMaterial)
	except:
		raise Http404('Material no trobat')
	
	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('materialpage.xml')
	elif parametre =="JSON":
		template = get_template('materialpage.js')	
	else:
		template = get_template('materialpage.html')
	gratacels=material.gratacel_set.all()
	
	variables = Context({
		'material': material,
		'gratacels': gratacels,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def arquitecte_list(request):
	try:
		arquitectes = Arquitecte.objects.all()
	except:
		raise Http404('Arquitectes no trobats')

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('arquitecte_list.xml')
	elif parametre =="JSON":
		template = get_template('arquitecte_list.js')	
	else:
		template = get_template('arquitecte_list.html')
	
	
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'arquitectes': arquitectes,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def material_list(request):
	try:
		materials = Material.objects.all()
	except:
		raise Http404('Materials no trobats')

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('material_list.xml')
	elif parametre =="JSON":
		template = get_template('material_list.js')	
	else:
		template = get_template('material_list.html')

	
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'materials': materials,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def estil_list(request):
	try:
		estils = Estil.objects.all()
	except:
		raise Http404('Materials no trobats')

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('estil_list.xml')
	elif parametre =="JSON":
		template = get_template('estil_list.js')	
	else:
		template = get_template('estil_list.html')

	
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'estils': estils,
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

def userpage(request, username):

	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		})
	output = template.render(variables)
	return HttpResponse(output)

class GratacelDetail (DetailView):
	model = Gratacel
	template_name = 'gratacelpage.html'

	def get_context_data(self, **kwargs):
		context = super(GratacelDetail, self).get_context_data(**kwargs)
		return context

class EstilDetail (DetailView):
	model = Estil
	template_name = 'estilpage.html'

	def get_context_data(self, **kwargs):
		context = super(EstilDetail, self).get_context_data(**kwargs)
		return context

class MaterialDetail (DetailView):
	model = Material
	template_name = 'materialpage.html'

	def get_context_data(self, **kwargs):
		context = super(MaterialDetail, self).get_context_data(**kwargs)
		return context

class ArquitecteDetail (DetailView):
	model = Arquitecte
	template_name = 'arquitectepage.html'

	def get_context_data(self, **kwargs):
		context = super(ArquitecteDetail, self).get_context_data(**kwargs)
		return context

#CREATES
	
class EstilCreate (CreateView):
	model = Estil
	template_name = 'form.html'
	form_class = EstilForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(EstilCreate, self).form_valid(form)

class MaterialCreate (CreateView):
	model = Material
	template_name = 'form.html'
	form_class = MaterialForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(MaterialCreate, self).form_valid(form)

class ArquitecteCreate (CreateView):
	model = Arquitecte
	template_name = 'form.html'
	form_class = ArquitecteForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ArquitecteCreate, self).form_valid(form)

class GratacelCreate (CreateView):
	model = Gratacel
	template_name = 'form.html'
	form_class = GratacelForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(GratacelCreate, self).form_valid(form)

#DELETES

class MaterialDelete(DeleteView):
	model = Material
	template_name = 'delete.html'
	success_url = reverse_lazy('material_list')

class EstilDelete(DeleteView):
	model = Estil
	template_name = 'delete.html'
	success_url = reverse_lazy('estil_list')

class ArquitecteDelete(DeleteView):
	model = Arquitecte
	template_name = 'delete.html'
	success_url = reverse_lazy('arquitecte_list')

class GratacelDelete(DeleteView):
	model = Gratacel
	template_name = 'delete.html'
	success_url = reverse_lazy('gratacel_list')

#API RESTFUL
class APIGratacelList(generics.ListCreateAPIView):
	model = Gratacel
	serializer_class = GratacelSerializer

class APIGratacelDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Gratacel
	serializer_class = GratacelSerializer

class APIEstilList(generics.ListCreateAPIView):
	model = Estil
	serializer_class = EstilSerializer

class APIEstilDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Estil
	serializer_class = EstilSerializer

class APIMaterialList(generics.ListCreateAPIView):
	model = Material
	serializer_class = MaterialSerializer

class APIMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Material
	serializer_class = MaterialSerializer

class APIArquitecteList(generics.ListCreateAPIView):
	model = Arquitecte
	serializer_class = ArquitecteSerializer

class APIArquitecteDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Arquitecte
	serializer_class = ArquitecteSerializer



#def login(request):	
#	if request.method== 'POST':
#		formulario= AutentificationForm (request.POST)
#		if formulario.is_valid:
#			usuario = request.POST['username']
#			clave = request.POSR['password']
#			acceso = authentificate(username=usuario, password=clave)
#			if acceso.is_active:
#				login(request, acceso)
#				template=get_template('userpage.html')
#			else:
#				template=get_template('login.html')

#def arquitectemain(request):
#
#	try:
#		arquitecte = Arquitecte.objects.all()
#	except:
#		raise Http404('No trobat cap arquitecte')
#
#	template = get_template('arquitectemain.html')
#	output = template.render()
#	return HttpResponse(output)


