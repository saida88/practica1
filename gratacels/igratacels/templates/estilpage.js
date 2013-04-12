{% if estil %}	
{
"estil":[{
	"idEstil" : {{ estil.idEstil }},
	"nomEstil" : {{ estil.nom }},
	"anyIniciEstil" : {{ estil.dataInici }},
	"anyFiEstil" : {{ estil.dataFi }},
	{% if gratacels %}
	"gratacels" : [ 
		{% for gratacel in gratacels %}
		{
			"idGratacel" : {{gratacel.idGratacel}},
			"nomGratacel" : {{gratacel.nom}},
			"altura" : {{ gratacel.altura }},
			"alturaTerrat" :  {{ gratacel.altura_terrat }},
			"numPlantes" : {{ gratacel.num_plantes }},
			"ciutat" : {{ gratacel.ciutat }},
			"anyGratacel" : {{ gratacel.any_inici }},
			"posicioRanquing" : {{ gratacel.posicio_ranquing }},
			"fotoGratacel" : {{gratacel.imatge}},
		}
		{% endfor %}
		]
	{% endif %}
}]
}
{% endif %}
