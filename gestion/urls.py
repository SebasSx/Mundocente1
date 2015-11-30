from django.conf.urls import  *

from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$','gestion.views.home',name='home'),
     #Login usuarios
    url(r'^ingresar/','gestion.views.ingresar',name='ingresar'),
    url(r'^logearse/','gestion.views.logearse',name='logearse'),
    url(r'^preguntar/','gestion.views.preguntar',name='preguntar'),
    url(r'^registrar/','gestion.views.registrar',name='registrar'),
    url(r'^guardar/','gestion.views.guardar',name='guardar'),
    



    # Salir 
    url(r'^salir/','gestion.views.salir',name='salir'),

	)