from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from models import *
from gestion.models import *
from django.http import HttpResponse,HttpResponseRedirect
import json



'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Valida el tipo de usuario para cargar la correspondiente pagina inicial
Funcion 		Gestion.4
'''

@login_required(login_url='/logearse')
def inicioDocente(request):
	tipo1 = TipoPublicacion.objects.filter(nombre_tipo='Convocatoria')
	tipo2 = TipoPublicacion.objects.filter(nombre_tipo='Evento')
	tipo3 = TipoPublicacion.objects.filter(nombre_tipo='Revista')
	convocatorias = Publicacion.objects.filter(tipo=tipo1)
	eventos = Publicacion.objects.filter(tipo=tipo2)
	revistas = Publicacion.objects.filter(tipo=tipo3)
	# areasC = AreasPublicacion.objects.filter(publicacion=convocatorias)
	# areasR = AreasPublicacion.objects.filter(publicacion=revistas)
	# areasE = AreasPublicacion.objects.filter(publicacion=eventos)
	credito =  Docente.objects.get(user=request.user)


	return render_to_response('inicioDocente.html',locals(), context_instance=RequestContext(request))
	


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Valida el tipo de usuario para cargar la correspondiente pagina inicial
Funcion 		Gestion.4
'''

@login_required(login_url='/logearse')
def descuentaCredito(request,idConvocatoria):
	us  = Docente.objects.get(user= request.user)
	us.credito  = us.credito -1
	us.save()
	data = {}
	data['credito'] = us.credito
	data['pk'] = idConvocatoria

	return HttpResponse(json.dumps(data), content_type = "application/json")
