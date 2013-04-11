# Create your views here.

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from igratacels.models import *

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
		template = get_template('gatacelpageXML.html')
	elif parametre =="JSON":
		template = get_template('gratacelpageJSON.html')	
	else:
		template = get_template('gratacelpage.html')
	arquitectes = gratacel.arquitectes.all()
	materials = gratacel.materials.all()
	estils = Estil.objects.get(idEstil=gratacel.idEstil_id)
	variables = Context({
		'gratacel': gratacel,
		'arquitectes': arquitectes,
		'estils': estils,
		'materials': materials
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
		template = get_template('gratacel_listXML.html')
	elif parametre =="JSON":
		template = get_template('gratacel_listJSON.html')	
	else:
		template = get_template('gratacel_list.html')

	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'gratacels': gratacels
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
		template = get_template('arquitectepageXML.html')
	elif parametre =="JSON":
		template = get_template('arquitectepageJSON.html')	
	else:
		template = get_template('arquitectepage.html')

	gratacels=arquitecte.gratacel_set.all()
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
	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('estilpageXML.html')
	elif parametre =="JSON":
		template = get_template('estilpageJSON.html')	
	else:
		template = get_template('estilpage.html')

	gratacels=estil.gratacel_set.all()	
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
	
	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('materialpageXML.html')
	elif parametre =="JSON":
		template = get_template('materialJSON.html')	
	else:
		template = get_template('materialpage.html')
	gratacels=material.gratacel_set.all()
	
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

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('arquitecte_listXML.html')
	elif parametre =="JSON":
		template = get_template('arquitecte_listJSON.html')	
	else:
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

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('material_listXML.html')
	elif parametre =="JSON":
		template = get_template('material_listJSON.html')	
	else:
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

	parametre = request.GET.get('format','')
	if parametre =="XML":
		template = get_template('estil_listXML.html')
	elif parametre =="JSON":
		template = get_template('estil_listJSON.html')	
	else:
		template = get_template('estil_list.html')

	
	variables = Context({
		'titlehead': 'Gratacels aPP',
		'pagetitle': 'Welcome to the Gratacels aPPlication',
		'contentbody': 'Managing non legal funding since 2013',
		'estils': estils
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


