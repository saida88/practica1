from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Restaurant, Dish, RestaurantReview

class GratacelSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='gratacel_detail')
	arquitectes = HyperlinkedRelatedField(many=True, read_only=True, view_name='gratacel_detail')
	materials = HyperlinkedRelatedField(many=True, read_only=True, view_name='gratacel_detail')
	idEstil = HyperlinkedRelatedField(many=False, read_only=True, view_name='gratacel_detail')
	user = CharField(read_only=True)

	class Meta:
		model = Restaurant
		fields = ('nom', 'altura', 'altura_terrat', 'num_plantes', 'ciutat', 'any_inici', 'idEstil', 'posicio_ranking', 			'arquitectes','materials', 'imatge','user','date')

class MaterialSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='material_detail')
	gratacel = HyperlinkedRelatedField(view_name='material_detail')
	user = CharField(read_only=True)

	class Meta:
		model = Material
		fields = ('nom', 'densitat', 'cost', 'user', 'date')

class EstilSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='estil_detail')
	gratacel = HyperlinkedRelatedField(view_name='estil_detail')
	user = CharField(read_only=True)

	class Meta:
		model = Estil
		fields = ('nom', 'dataInici', 'dataFi', 'user', 'date')

class ArquitecteSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='arquitecte_detail')
	gratacel = HyperlinkedRelatedField(view_name='arquitecte_detail')
	user = CharField(read_only=True)

	class Meta:
		model = Arquitecte
		fields = ('nom', 'cognom', 'data_naixement', 'data_defuncio', 'nacionalitat', 'imatge', 'user', 'date')
