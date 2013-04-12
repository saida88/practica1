{% if estils %}
{
"estils":[{
{% for estil in estils %}
	"estil":[
		"idEstil":{{ estil.idEstil }}
		"nomEstil":{{ estil.nom }}
		"anyIniciEstil":{{ estil.dataInici }}
		"anyFiEstil":{{ estil.dataFi }}
	]}
{% endfor %}
	]
{% endif %}
