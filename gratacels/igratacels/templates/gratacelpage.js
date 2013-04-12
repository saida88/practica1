<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE SYSTEM "exemple.dtd">

{% if gratacel %}
<gratacel>
	<idGratacel>{{gratacel.idGratacel}}</idGratacel>
	<nomGratacel>{{gratacel.nom}}</nomGratacel>
	<altura>{{ gratacel.altura }}</altura>
	<alturaTerrat>{{ gratacel.altura_terrat }}</alturaTerrat>
	<numPlantes>{{ gratacel.num_plantes }}</numPlantes>
	<ciutat>{{ gratacel.ciutat }}</ciutat>
	<anyGratacel>{{ gratacel.any_inici }}</anyGratacel>
	<posicioRanquing>{{ gratacel.posicio_ranquing }}</posicioRanquing>
	<fotoGratacel>{{gratacel.imatge}}</fotoGratacel>
	{% if estils %}	
		<estil>
			<idEstil>{{ estils.idEstil }}</idEstil>
			<nomEstil>{{ estils.nom }}</nomEstil>
			<anyIniciEstil>{{ estils.dataInici }}</anyIniciEstil>
			<anyFiEstil>{{ estils.dataFi }}</anyFiEstil>
		</estil>
	{% endif %}

	{% if arquitectes %}
		<arquitectes>
		{% for arquitecte in arquitectes %}
		<arquitecte>
			<idArquitecte>{{arquitecte.idArquitecte}}</idArquitecte>
			<nomArquitecte>{{arquitecte.nom}}</nomArquitecte>
			<cognomArquitecte>{{arquitecte.cognom}}</cognomArquitecte>
			<dataNaixement>{{arquitecte.data_naixement}}</dataNaixement>
			<dataDefuncio>{{arquitecte.data_defuncio}}</dataDefuncio>
			<nacionalitat>{{arquitecte.nacionalitat}}</nacionalitat>
			<fotoArquitecte>{{arquitecte.imatge}}</fotoArquitecte>
		</arquitecte>
		{% endfor %}
	</arquitectes>
	{% endif %}

	{% if materials %}
		<materials>
		{% for material in materials %}
		<material>
			<idMaterial>{{material.idMaterial}}</idMaterial>
			<nomMaterial>{{material.nom}}</nomMaterial>
			<cost>{{material.cost}}</cost>
			<densitat>{{material.densitat}}</densitat>
		</material>
		{% endfor %}
		</materials>
	{% endif %}
</gratacel>
{% endif %}
