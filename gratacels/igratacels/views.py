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

	try:
		relacio_arquitecte_gratacel =Gratacel_arquitectes.objects.get(idArquitecte=idArquitecte)
	except:
		raise Http404('Arquitecte no te gratacels')

	gratacels=arquitecte.gratacel_set.all()
	template = get_template('arquitectepage.html')
	variables = Context({
		'idArquitecte': idArquitecte,
		'gratacels': gratacels
		})
	output = template.render(variables)
	return HttpResponse(output)

