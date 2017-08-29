from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Site_tmp)
admin.site.register(models.Tipo)
admin.site.register(models.Subtipo)
admin.site.register(models.Objeto_tmp)
admin.site.register(models.FotoObjeto_tmp)
admin.site.register(models.FotoSitio_tmp)
admin.site.register(models.Site3)