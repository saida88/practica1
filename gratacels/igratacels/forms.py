from django.forms import ModelForm
from models import *

class EstilForm(ModelForm):
	class Meta:
		model = Estil
		exclude = ('user', 'date', 'idEstil')

class MaterialForm(ModelForm):
	class Meta:
		model = Material
		exclude = ('user', 'date', 'idMaterial')

class ArquitecteForm(ModelForm):
	class Meta:
		model = Arquitecte
		exclude = ('user', 'date', 'idArquitecte')

class GratacelForm(ModelForm):
	class Meta:
		model = Gratacel
		exclude = ('user', 'date', 'idGratacel', 'idEstil', 'arquitectes', 'materials')
