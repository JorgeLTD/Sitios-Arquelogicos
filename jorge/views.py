from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import *
from core.models import *


# Vistas Jorge
# funcionando, falta añadir boton agregar imagen o listar objetos
def new_object(request, site_pk):
	tipos = Tipo.objects.all()
	subtipos = Subtipo.objects.all()

	if request.method == 'POST':
		name = request.POST.get('nombre')
		description = request.POST.get('descripcion')
		subtype = Subtipo.objects.get(pk=request.POST.get('subtipo'))
		sitio = Site_tmp.objects.get(pk=site_pk)
		# pdb.set_trace()
		nuevo_objeto = Objeto_tmp(nombre=name, descripcion=description, subtipo=subtype, sitio=sitio)
		nuevo_objeto.save()

		return redirect('jorge:list_objects', site_pk)

	return render(request, 'objects/new_object.html', {'tipos': tipos, 'subtipos': subtipos})


# sin testear a full
def new_image_object(request, object_pk):
	objeto = get_object_or_404(Objeto_tmp, pk=object_pk)

	if request.method == 'POST':
		form = FotosObjetoForm(request.POST, request.FILES)
		if form.is_valid():
			new_foto = form.save(commit=False)
			new_foto.objeto = objeto
			new_foto.save()
			if 'terminar' == request.POST.get('action'):
				print('redireccion')
				return redirect('jorge:list_objects', objeto.sitio.pk)
		else:
			print('ERROR EN EL GUARDADO')
			fotos = FotoObjeto_tmp.objects.filter(objeto_id=object_pk)
			return render(request, 'objects/new_image_object.html', {'form': form, 'fotos': fotos})

	# formulario vacio y fotos actuales
	form = FotosObjetoForm()
	fotos = FotoObjeto_tmp.objects.filter(objeto_id=object_pk)
	return render(request, 'objects/new_image_object.html', {'form': form, 'fotos': fotos})


# funcionando
def list_sites(request):
	sites = Site_tmp.objects.all()
	return render(request, 'sites/list_sites.html', {'sites': sites})


# funcionando
def list_objects(request, site_pk):
	sitio = Site_tmp.objects.get(pk=site_pk)
	objs = Objeto_tmp.objects.filter(sitio__pk=site_pk)

	return render(request, 'objects/list_object.html', {'objs': objs, 'sitio': sitio})


# funcionando
def edit_object(request, object_pk):
	old_obj = get_object_or_404(Objeto_tmp, pk=object_pk)
	tipos = Tipo.objects.all()
	subtipos = Subtipo.objects.all()

	if request.method == 'POST':
		name = request.POST.get('nombre')
		description = request.POST.get('descripcion')
		subtype = Subtipo.objects.get(pk=request.POST.get('subtipo'))
		# actualizar
		old_obj.nombre = name
		old_obj.descripcion = description
		old_obj.subtipo = subtype
		old_obj.save()
		return redirect('jorge:list_objects', old_obj.sitio.pk)

	return render(request, 'objects/edit_object.html', {'old_obj': old_obj, 'tipos': tipos, 'subtipos': subtipos})


# funcionando, falta borrar los archivos asociados y thumbanails
def delete_object(request, object_pk):
	obj = Objeto_tmp.objects.get(pk=object_pk)
	site_pk = obj.sitio.pk
	fotos = FotoObjeto_tmp.objects.filter(objeto=obj)

	for foto in fotos:
		foto.delete()

	obj.delete()

	return redirect('jorge:list_objects', site_pk)


# TODO: slide para mostrar fotos
def gallery_objects(request):
	objs = Objeto_tmp.objects.all()
	return render(request, 'gallery/gallery_objects.html', {'objs': objs})


# TODO: calcular paginas para seleccionar
def gallery_sites(request, page=1):
	# cambiar Site_tmp por Site3
	lista_sitios = Site_tmp.objects.all().order_by('id')
	paginator = Paginator(lista_sitios, 16)
	try:
		sitios = paginator.page(page)
	except PageNotAnInteger:
		sitios = paginator.page(1)
	except EmptyPage:
		sitios = paginator.page(paginator.num_pages)

	return render(request, 'gallery/gallery_sites.html', {'sitios': sitios})


# sin testear a full
def new_image_site(request, site_pk):
	sitio = get_object_or_404(Site_tmp, pk=site_pk)

	if request.method == 'POST':
		form = FotosSitioForm(request.POST, request.FILES)
		if form.is_valid():
			new_foto = form.save(commit=False)
			new_foto.sitio = sitio
			new_foto.save()
			if 'terminar' == request.POST.get('action'):
				print('redireccion')
				return redirect('jorge:list_sites')
		else:
			print('ERROR EN EL GUARDADO')
			fotos = FotoSitio_tmp.objects.filter(sitio_id=site_pk)
			return render(request, 'sites/new_image_site.html', {'form': form, 'fotos': fotos})

	# formulario vacio y fotos actuales
	form = FotosSitioForm()
	fotos = FotoSitio_tmp.objects.filter(sitio_id=site_pk)
	return render(request, 'sites/new_image_site.html', {'form': form, 'fotos': fotos})


# TODO: falta borrar archivo y thumbnail
def delete_photo_object(request, photo_pk):
	foto = FotoObjeto_tmp.objects.get(pk=photo_pk)
	obj_pk = foto.objeto.pk
	foto.delete()
	return redirect('jorge:new_image_object', obj_pk)


# TODO: falta borrar archivo y thumbnail
def delete_photo_site(request, photo_pk):
	foto = FotoSitio_tmp.objects.get(pk=photo_pk)
	site_pk = foto.sitio.pk
	foto.delete()
	return redirect('jorge:new_image_site', site_pk)


def object_page(request, object_pk):
	obj = get_object_or_404(Objeto_tmp, pk=object_pk)

	return render(request, 'objects/object_page.html', {'obj': obj})
