# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from igratacels.models import *

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013'
		})
	output = template.render(variables)
	return HttpResponse(output)

def arquitectepage(request, idArquitecte):

	try:
		arquitecte =Arquitecte.objects.get(idArquitecte=idArquitecte)
	except:
		raise Http404('Arquitecte no trobat')

	gratacels=arquitecte.gratacel_set.all()
	template = get_template('arquitectepage.html')
	variables = Context({
		'idArquitecte': idArquitecte,
		'gratacels': gratacels
		})
	output = template.render(variables)
	return HttpResponse(output)

def estilpage(request, idEstil):

	try:
		estil = Estil.objects.get(idEstil=idEstil)
	except:
		raise Http404('Estil no trobat')

	gratacels=estil.gratacel_set.all()
	template = get_template('estilpage.html')
	variables = Context({
		'idEstil': idEstil,
		'gratacels': gratacels
		})
	output = template.render(variables)
	return HttpResponse(output)

def materialpage(request, idMaterial):

	try:
		material = Material.objects.get(idMaterial=idMaterial)
	except:
		raise Http404('Material no trobat')

	gratacels=material.gratacel_set.all()
	template = get_template('materialpage.html')
	variables = Context({
		'idMaterial': idMaterial,
		'gratacels': gratacels
		})
	output = template.render(variables)
	return HttpResponse(output)
