from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=30)
	slug = models.SlugField()

	
	def __str__(self):
		return self.nombre + " " + self.slug 

	def __unicode__(self):
		return self.nombre + " " + self.slug 


class Articulo(models.Model):
	titulo = models.CharField(max_length=30)
	slug = models.SlugField()
	contenido = models.TextField()
	imagen = models.ImageField(upload_to = 'fotos_articulos')
	autor = models.ForeignKey(User, related_name="articulos")

	categoria = models.ManyToManyField(Categoria)

	def __str__(self):
		return self.titulo + " " + self.slug 

	def __unicode__(self):
		return self.titulo + " " + self.slug 

