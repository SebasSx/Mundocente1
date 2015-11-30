from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext




'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		16 Nov 2015
Descripcion  	Valida el tipo de usuario para cargar la correspondiente pagina inicial
Funcion 		Gestion.4
'''

@login_required(login_url='/logearse')
def inicioRevistas(request):
	return render_to_response('inicioRevistas.html',locals(), context_instance=RequestContext(request))
		
