{% if arquitecte %}
{
"arquitecte":[{
	"idArquitecte" : {{arquitecte.idArquitecte}},
	"nomArquitecte" : {{arquitecte.nom}},
	"cognomArquitecte" : {{arquitecte.cognom}},
	"dataNaixement" : {{arquitecte.data_naixement}},
	"dataDefuncio" : {{arquitecte.data_defuncio}},
	"nacionalitat" : {{arquitecte.nacionalitat}},
	"fotoArquitecte" : {{arquitecte.imatge}},
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
