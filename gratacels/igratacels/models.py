from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Arquitecte (models.Model):
	idArquitecte = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	cognom = models.TextField(max_length=25)
	data_naixement = models.DateField()
	data_defuncio = models.DateField(blank=True,null=True)
	nacionalitat = models.TextField(max_length=25)
	imatge = models.TextField()
	user = models.ForeignKey(User)
	date = models.DateField(default=date.today)

	def __unicode__(self):
		return u"%s, %s" % (self.cognom, self.nom)
	def get_absolute_url(self):
		return reverse('arquitecte_detail', kwargs={'idArquitecte': self.pk})

class Material (models.Model):
	idMaterial = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	densitat = models.FloatField()
	cost = models.FloatField()
	user = models.ForeignKey(User)
	date = models.DateField(default=date.today)

	def __unicode__(self):
		return u"%s" % self.nom
	def get_absolute_url(self):
		return reverse('material_detail', kwargs={'idMaterial': self.pk})

class Estil (models.Model): 
	idEstil = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	dataInici = models.IntegerField(max_length=4)
	dataFi = models.IntegerField(max_length=4, blank = True,null=True)
	user = models.ForeignKey(User)
	date = models.DateField(default=date.today)

	def __unicode__(self):
		return u"%s" % self.nom
	def get_absolute_url(self):
		return reverse('estil_detail', kwargs={'idEstil': self.pk})

class Gratacel (models.Model):
	idGratacel = models.AutoField(primary_key=True)
	nom = models.TextField(max_length=25)
	altura = models.IntegerField()
	altura_terrat = models.IntegerField()
	num_plantes = models.IntegerField()
	ciutat = models.TextField(max_length=25)
	pais = models.TextField(max_length=25)
	any_inici = models.IntegerField()
	idEstil = models.ForeignKey(Estil)
	posicio_ranking = models.IntegerField(blank=True, null=True)
	arquitectes = models.ManyToManyField(Arquitecte)
	materials = models.ManyToManyField(Material)
	imatge = models.TextField()
	user = models.ForeignKey(User)
	date = models.DateField(default=date.today)
	
	def __unicode__(self):
		return u"%s" % self.nom
	def get_absolute_url(self):
		return reverse('gratacel_detail', kwargs={'idGratacel': self.pk})
	def averageRating(self):
		countTotal = 0.0
		countNum = 0
		for review in self.gratacelreview_set.all():
			countNum +=1
			countTotal += review.rating
		return countTotal/countNum

class Review(models.Model):
    RATING_CHOICES = ((1, '1'), (2, '2'), (3,'3'), (4,'4'), (5, '5'))	 	
    rating  =  models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)	
    comment = models.TextField(blank=True,  null=True)	
    user  =  models.ForeignKey(User)	
    date = models.DateField(default=date.today)	
    #class Meta:	
	#abstract  =  True	
  
class GratacelReview(Review):
    gratacel = models.ForeignKey(Gratacel)


