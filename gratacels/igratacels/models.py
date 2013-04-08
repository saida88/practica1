from django.db import models

# Create your models here.

class Arquitecte (models.Model):
	idArquitecte = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	cognom = models.TextField(max_length=25)
	data_naixement = models.DateField()
	data_defuncio = models.DateField(blank=True,null=True)
	nacionalitat = models.TextField(max_length=25)
	imatge = models.TextField()

class Material (models.Model):
	idMaterial = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	densitat = models.FloatField()
	cost = models.FloatField()

class Estil (models.Model): 
	idEstil = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	dataInici = models.IntegerField(max_length=4)
	dataFi = models.IntegerField(max_length=4, blank = True,null=True)

class Gratacel (models.Model):
	idGratacel = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	altura = models.IntegerField()
	altura_terrat = models.IntegerField()
	num_plantes = models.IntegerField()
	ciutat = models.TextField(max_length=25)
	any_inici = models.IntegerField()
	idEstil = models.ForeignKey(Estil)
	posicio_ranking = models.IntegerField(blank=True, null=True)
	arquitectes = models.ManyToManyField(Arquitecte)
	materials = models.ManyToManyField(Material)
	imatge = models.TextField()

#class GratacelsArquitecte (models.Model):
#	idGratacel = models.ForeignKey(Gratacel, primary_key=True)
#	idArquitecte = models.ForeignKey(Arquitecte, primary_key=True)

#class GratacelsMaterials (models.Model):
#	idGratacel = models.ForeignKey(Gratacel, primary_key=True)
#	idMaterial = models.ForeignKey(Materials, primary_key=True)

	
	
