from django.db import models

# Create your models here.

class Arquitecte (models.Model):
	idArquitecte = models.IntegerField(primary_key=True)
	nom = models.TextField(max_length=25)
	cognom = models.TextField(max_length=25)
	data_naixement = models.DateTimeField()
	nacionalitat = models.TextField(max_length=25)

class Materials (models.Model):
	idMaterial = models.IntegerField(primary_key=True)
	nom = models.TextField(max_length=25)
	densitat = models.FloatField()
	cost = models.FloatField()

class Estil (models.Model): 
	idEstil = models.IntegerField(primary_key=True)
	nom = models.TextField(max_length=25)
	data_inici = models.DateTimeField()
	data_fi = models.DateTimeField()

class Gratacel (models.Model):
	idGratacel = models.IntegerField(primary_key=True)
	nom = models.TextField(max_length=25)
	superficie = models.IntegerField()
	altura = models.IntegerField()
	altura_terrat = models.IntegerField()
	num_plantes = models.IntegerField()
	ciutat = models.TextField(max_length=25)
	any_inici = models.IntegerField()
	idEstil = models.ForeignKey(Estil)
	posicio_ranking = models.IntegerField()
	arquitectes = models.ManyToManyField(Arquitecte)
	materials = models.ManyToManyField(Materials)

#class GratacelsArquitecte (models.Model):
#	idGratacel = models.ForeignKey(Gratacel, primary_key=True)
#	idArquitecte = models.ForeignKey(Arquitecte, primary_key=True)

#class GratacelsMaterials (models.Model):
#	idGratacel = models.ForeignKey(Gratacel, primary_key=True)
#	idMaterial = models.ForeignKey(Materials, primary_key=True)

	
	
