from django.db import models
from django.contrib.auth.models import User



class Universidad(models.Model):
	user = models.OneToOneField(User)
	nombre_universidad = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_universidad

class Revista(models.Model):
	user = models.OneToOneField(User)
	nombre_revista = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_revista

class Docente(models.Model):
	user = models.OneToOneField(User)
	telefono = models.CharField(max_length=250)
	credito = models.IntegerField()
	def __unicode__(self):
		return self.user.username

class Area(models.Model):
	nombre_area = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_area

class TipoPublicacion(models.Model):
	nombre_tipo = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_tipo

class Docente_Area(models.Model):
	docente = models.ForeignKey(Docente,blank=None,null=None)
	area = models.ForeignKey(Area,blank=None,null=None)
	def __unicode__(self):
		return '%s %s' % (self.docente,self.area)

class Publicacion(models.Model):
	universidad = models.ForeignKey(Universidad,blank=True,null=True)
	descripcion = models.CharField(max_length=300)
	fecha_inicio = models.DateField(auto_now=False)
	fecha_fin = models.DateField(auto_now=False)
	lugar = models.CharField(max_length=300)
	link = models.CharField(max_length=350)
	tipo = models.ForeignKey(TipoPublicacion)
	def __unicode__(self):
		return self.descripcion

class AreasPublicacion(models.Model):
	area = models.ForeignKey(Area,blank=None,null=None)
	publicacion = models.ForeignKey(Publicacion,blank=None,null=None)
	def __unicode__(self):
		return '%s %s' % (self.area,self.publicacion)





