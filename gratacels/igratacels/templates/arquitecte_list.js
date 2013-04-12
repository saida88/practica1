{% if arquitectes %}
{
"arquitectes" :[
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
}
{% endif %}
