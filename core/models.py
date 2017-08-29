from django.db import models


class Site3(models.Model):
	name = models.CharField(max_length=32, verbose_name='nombre', blank=True)

	# jorge nuevo lunes
	def getimage(self):
		img = FotoSitio.objects.filter(sitio_id=self.pk).first()
		return img

	# jorge nuevo lunes
		imgs = FotoSitio.objects.filter(sitio_id=self.pk).first()
		return imgs


class Site_tmp(models.Model):
	name = models.CharField(max_length=32, verbose_name='nombre')
	descripcion = models.CharField(max_length=128, null=True, blank=True)

	# otros parametros no son relevantes en mi parte

	def __str__(self):
		return self.name

	# jorge nuevo lunes
	def getimage(self):
		img = FotoSitio_tmp.objects.filter(sitio_id=self.pk).first()
		return img

	# jorge nuevo lunes
	def getimages(self):
		imgs = FotoSitio_tmp.objects.filter(sitio_id=self.pk)
		return imgs


# TABLAS JORGE, copiar y pegar en mismo orden
class Tipo(models.Model):
	nombre = models.CharField(max_length=32, verbose_name='tipo', blank=False, null=False)

	def __str__(self):
		return self.nombre


class Subtipo(models.Model):
	nombre = models.CharField(max_length=32, verbose_name='subtipo', blank=False, null=False)
	tipo = models.ForeignKey(Tipo, null=False)

	def __str__(self):
		return self.nombre


class Objeto_tmp(models.Model):
	nombre = models.CharField(max_length=32, verbose_name='Objeto_tmp')
	descripcion = models.CharField(max_length=256, verbose_name='Descripcion')
	sitio = models.ForeignKey(Site_tmp, on_delete=models.CASCADE)
	subtipo = models.ForeignKey(Subtipo, on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.nombre)

	def getimage(self):
		img = FotoObjeto_tmp.objects.filter(objeto_id=self.pk).first()
		return img

	def getimages(self):
		imgs = FotoObjeto_tmp.objects.filter(objeto_id=self.pk)
		return imgs


class Objeto(models.Model):
	nombre = models.CharField(max_length=32, verbose_name='Objeto_tmp')
	descripcion = models.CharField(max_length=256, verbose_name='Descripcion')
	sitio = models.ForeignKey(Site3, on_delete=models.CASCADE)
	subtipo = models.ForeignKey(Subtipo, on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.nombre)

	def getimage(self):
		img = FotoObjeto.objects.filter(objeto_id=self.pk).first()
		return img

	def getimages(self):
		imgs = FotoObjeto.objects.filter(objeto_id=self.pk)
		return imgs


class FotoObjeto_tmp(models.Model):
	autor = models.CharField(max_length=64, verbose_name='autor', blank=True)
	descripcion = models.CharField(max_length=256, verbose_name='descripcion', blank=True)
	archivo = models.ImageField(upload_to='img_objects', blank=False)
	objeto = models.ForeignKey(Objeto_tmp, null=False, blank=False)

	def __str__(self):
		return "{} // obj_id = {}".format(self.descripcion, self.objeto.pk)


class FotoObjeto(models.Model):
	autor = models.CharField(max_length=64, verbose_name='autor', blank=True)
	descripcion = models.CharField(max_length=256, verbose_name='descripcion', blank=True)
	archivo = models.ImageField(upload_to='img_objects', blank=False)
	objeto = models.ForeignKey(Objeto, null=False, blank=False)

	def __str__(self):
		return "{} // obj_id = {}".format(self.descripcion, self.objeto.pk)


class FotoSitio_tmp(models.Model):
	autor = models.CharField(max_length=64, verbose_name='autor', blank=True)
	descripcion = models.CharField(max_length=256, verbose_name='descripcion', blank=True)
	archivo = models.ImageField(upload_to='img_sites', blank=False, null=False)
	sitio = models.ForeignKey(Site_tmp, blank=False, null=False, )


class FotoSitio(models.Model):
	autor = models.CharField(max_length=64, verbose_name='autor', blank=True)
	descripcion = models.CharField(max_length=256, verbose_name='descripcion', blank=True)
	archivo = models.ImageField(upload_to='img_sites', blank=False, null=False)
	sitio = models.ForeignKey(Site3, blank=False, null=False, )