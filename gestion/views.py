from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from models import *
from django.contrib.auth.models import Group




# Create your views here.

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Pregunta si el usuario esta logueado y envia a ingresar o preguntar tipo usuario
Funcion 		Gestion.1
'''
def home(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/preguntar')
	return HttpResponseRedirect('/ingresar')
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la vista del login
Funcion 		Gestion.2
'''
def ingresar(request):
	return render_to_response('Login.html',locals(),context_instance=RequestContext(request))
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Recibe parametros del login,autentica el usuario en la db,
Funcion 		Gestion.3
'''
def logearse(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/preguntar')
				else:
					return render_to_response('no_activo.html', context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/ingresar')
	return render_to_response('log.html',{'formulario':formulario}, context_instance=RequestContext(request))

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Valida el tipo de usuario para cargar la correspondiente pagina inicial
Funcion 		Gestion.4
'''
@login_required(login_url='/logearse')
def preguntar(request):
	
	grupo = request.user.groups.all()[0].name 

	if 	grupo=='Universidad' :
	 	return HttpResponseRedirect('/inicioUniversidad')
	elif grupo=='Docente':
	 	return HttpResponseRedirect('/inicioDocente')
	elif grupo=='Revista':
	 	return HttpResponseRedirect('/inicioRevistas')
	
	return HttpResponse('no hay tipo usuario')
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Finaliza session 
Funcion 		Gestion.5
'''
@login_required(login_url='/logearse')
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza html de registrar usuario 
Funcion 		Gestion.5
'''
def registrar(request):
	return render_to_response('Registro.html',locals(), context_instance=RequestContext(request))

def guardar(request):
	if request.method == 'POST':
		try:
			existe = User.objects.get(username=request.POST['username'])
			mensaje= 'El Usuario ya existe'
			return render_to_response('Registro.html',locals(), context_instance=RequestContext(request))
		except Exception, e:
			user = User.objects.create_user(request.POST['username'],None,request.POST['password'])
			user.email=request.POST['email']
			user.first_name= request.POST['nombre']
			user.last_name = request.POST['apellido']
			user.is_active = True
			user.save()
			docente = Docente()

			if request.POST['tipo']=='Docente':
				g = Group.objects.get(name='Docente') 
				g.user_set.add(user)
				docente.telefono = request.POST['telefono']
				docente.credito = request.POST['credito']
				docente.user = user
				docente.save()
	return HttpResponseRedirect('/')