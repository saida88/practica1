{% if materials %}
{
"materials":[
	{% for material in materials %}
	{
		"idMaterial" : {{material.idMaterial}},
		"nomMaterial" : {{material.nom}},
		"cost" : {{material.cost}},
		"densitat" : {{material.densitat}},
	}
	{% endfor %}
]
}
{% endif %}
