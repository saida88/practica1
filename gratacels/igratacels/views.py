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

#def gratacelpage(request, idGratacel):
#
#	try:
#		gratacel = Gratacel.objects.get(idGratacel=idGratacel)
#	except:
#		raise Http404('Gratacel no trobat')
#
#	arquitectes = gratacel.arquitecte_set.all()
#	materials = gratacel.material_set.all()
#	estils = gratacel.estil_set.all()
#	template = get_template('gratacelpage.html')
#	variables = Context({
#		'gratacel': gratacel,
#		'arquitectes': arquitectes,
#		'estils': estils,
#		'materials': materials
#		})
#	output = template.render(variables)
#	return HttpResponse(output)

def arquitectepage(request, idArquitecte):

	try:
		arquitecte =Arquitecte.objects.get(idArquitecte=idArquitecte)
	except:
		raise Http404('Arquitecte no trobat')

	gratacels=arquitecte.gratacel_set.all()
	template = get_template('arquitectepage.html')
	variables = Context({
		'arquitecte': arquitecte,
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
		'estil': estil,
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
		'material': material,
		'gratacels': gratacels
		})
	output = template.render(variables)
	return HttpResponse(output)

def arquitecte_list(request):
	try:
		arquitectes = Arquitecte.objects.all()
	except:
		raise Http404('Arquitectes no trobats')

	template = get_template('arquitecte_list.html')
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'arquitectes': arquitectes
		})
	output = template.render(variables)
	return HttpResponse(output)

def material_list(request):
	try:
		materials = Material.objects.all()
	except:
		raise Http404('Materials no trobats')

	template = get_template('material_list.html')
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'materials': materials
		})
	output = template.render(variables)
	return HttpResponse(output)

def estil_list(request):
	try:
		estils = Estil.objects.all()
	except:
		raise Http404('Materials no trobats')

	template = get_template('estil_list.html')
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'estils': estils
		})
	output = template.render(variables)
	return HttpResponse(output)


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


