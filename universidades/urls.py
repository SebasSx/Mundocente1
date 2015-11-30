from django.conf.urls import  *

from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^inicioUniversidad/','universidades.views.inicioUniversidad',name='inicioUniversidad'),
    url(r'^agregarConvocatoria/','universidades.views.agregarConvocatoria',name='agregarConvocatoria'),
    url(r'^agregarRevista/','universidades.views.agregarRevista',name='agregarRevista'),
    url(r'^agregarEvento/','universidades.views.agregarEvento',name='agregarEvento'),

    url(r'^formularioConvocatoria/','universidades.views.formularioConvocatoria',name='formularioConvocatoria'),
    url(r'^addConvocatoria/','universidades.views.addConvocatoria',name='addConvocatoria'),
    
	)