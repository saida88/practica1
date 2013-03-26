from django.db import models

# Create your models here.

class Arquitecte (models.Model):
	idArquitecte = models.IntegerField(primary_key=True)
	nom = models.TextField(max_length=25)
	cognom = models.TextField(max_length=25)
	data_naixement = models.DateTimeField()
	nacionalitat = models.TextField(max_length=25)
