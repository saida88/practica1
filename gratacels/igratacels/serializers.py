from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class GratacelSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='gratacel-detail')
	arquitectes = HyperlinkedRelatedField(many=True, read_only=True, view_name='arquitecte-detail')
	materials = HyperlinkedRelatedField(many=True, read_only=True, view_name='material-detail')
	idEstil = HyperlinkedRelatedField(many=False, read_only=True, view_name='estil-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Gratacel
		fields = ('nom', 'altura', 'altura_terrat', 'num_plantes', 'ciutat', 'any_inici', 'idEstil', 'posicio_ranking', 			'arquitectes','materials', 'imatge','user','date')

class MaterialSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='material-detail')
	gratacel_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='gratacel-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Material
		fields = ('nom', 'densitat', 'cost', 'user', 'date',  'gratacel_set')

class EstilSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='estil-detail')
	gratacel_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='gratacel-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Estil
		fields = ('nom', 'dataInici', 'dataFi', 'user', 'date',  'gratacel_set')

class ArquitecteSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='arquitecte-detail')
	gratacel_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='gratacel-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Arquitecte
		fields = ('nom', 'cognom', 'data_naixement', 'data_defuncio', 'nacionalitat', 'imatge', 'user', 'date',)# 'gratacel')
