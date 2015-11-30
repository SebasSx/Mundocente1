from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from models import *
from gestion.models import *
from django.contrib.auth.models import User
from datetime import datetime 




'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		16 Nov 2015
Descripcion  	Valida el tipo de usuario para cargar la correspondiente pagina inicial
Funcion 		Gestion.4
'''

@login_required(login_url='/logearse')
def inicioUniversidad(request):
	universidad =  Universidad.objects.get(user=request.user)
	tipo1 = TipoPublicacion.objects.filter(nombre_tipo='Convocatoria')
	tipo2 = TipoPublicacion.objects.filter(nombre_tipo='Evento')
	tipo3 = TipoPublicacion.objects.filter(nombre_tipo='Revista')
	convocatorias = Publicacion.objects.filter(tipo=tipo1, universidad=universidad)
	eventos = Publicacion.objects.filter(tipo=tipo2,universidad=universidad)
	revistas = Publicacion.objects.filter(tipo=tipo3,universidad=universidad)
	return render_to_response('inicioUniversidad.html',locals(), context_instance=RequestContext(request))
		
@login_required(login_url='/logearse')
def agregarConvocatoria(request):
	return render_to_response('agregarConvocatoria.html',locals(), context_instance=RequestContext(request))

@login_required(login_url='/logearse')
def agregarRevista(request):
	return render_to_response('agregarRevista.html',locals(), context_instance=RequestContext(request))
			
@login_required(login_url='/logearse')
def agregarEvento(request):
	return render_to_response('agregarEvento.html',locals(), context_instance=RequestContext(request))

@login_required(login_url='/logearse')
def formularioConvocatoria(request):
	if agregarConvocatoria(request):
		areas = Area.objects.all()
		return render_to_response('agregarConvocatoria.html',locals(), context_instance=RequestContext(request))		
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def addConvocatoria(request):
	if agregarConvocatoria(request):
		#usdcmi o obe elstalssdjs
		admin =  Universidad.objects.get(user=request.user)
		cargo = request.POST['descripcion']
		fecha_inicio =  datetime.strptime(request.POST['fecha_inicio'], '%d %B, %Y').date()  
		fecha_fin = datetime.strptime(request.POST['fecha_fin'], '%d %B, %Y').date()  
		link = request.POST['link']
		lugar = request.POST['lugar']
		areas = Area.objects.get(pk=request.POST['area'])

		# si tipo es una llave foranea tiene que traer el objeto 
		tipo = request.POST['tipo']
		t  = TipoPublicacion.objects.get(pk=1)
		convocatoria= Publicacion(universidad=admin, descripcion=cargo, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, lugar=lugar, link=link, tipo=t)
		convocatoria.save()
		areasPublicacion = AreasPublicacion(area=areas, publicacion=convocatoria)
		areasPublicacion.save()
		return HttpResponseRedirect('/inicioUniversidad/')
	return HttpResponseRedirect('/')					