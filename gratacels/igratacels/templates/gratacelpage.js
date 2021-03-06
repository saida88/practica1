{% if gratacel %}
{
"gratacel":[
	"idGratacel" : {{gratacel.idGratacel}},
	"nomGratacel" : {{gratacel.nom}},
	"altura" : {{ gratacel.altura }},
	"alturaTerrat" : {{ gratacel.altura_terrat }},
	"numPlantes" : {{ gratacel.num_plantes }},
	"ciutat" : {{ gratacel.ciutat }},
	"anyGratacel" : {{ gratacel.any_inici }},
	"posicioRanquing" : {{ gratacel.posicio_ranquing }},
	"fotoGratacel" : {{gratacel.imatge}},
	{% if estils %}	
		"estil" : {
			"idEstil" : {{ estils.idEstil }},
			"nomEstil" : {{ estils.nom }},
			"anyIniciEstil" : {{ estils.dataInici }},
			"anyFiEstil" : {{ estils.dataFi }},
			}
	{% endif %}

	{% if arquitectes %}
		"arquitectes" : [
		{% for arquitecte in arquitectes %}
			{
			"idArquitecte" : {{arquitecte.idArquitecte}},
			"nomArquitecte" : {{arquitecte.nom}},
			"cognomArquitecte" : {{arquitecte.cognom}},
			"dataNaixement" : {{arquitecte.data_naixement}},
			"dataDefuncio" : {{arquitecte.data_defuncio}},
			"nacionalitat" : {{arquitecte.nacionalitat}},
			"fotoArquitecte" : {{arquitecte.imatge}},
			}
		{% endfor %}
		]
	{% endif %}

	{% if materials %}
		"materials" : [
		{% for material in materials %}
			{
			"idMaterial" : {{material.idMaterial}},
			"nomMaterial" : {{material.nom}},
			"cost" : {{material.cost}},
			"densitat" : {{material.densitat}},
			}
		{% endfor %}
		]
	{% endif %}
}]
}
{% endif %}
