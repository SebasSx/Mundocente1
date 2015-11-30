from django.conf.urls import  *

from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),


    url(r'^inicioDocente/','docentes.views.inicioDocente',name='inicioDocente'),
    url(r'^descuentaCredito/(?P<idConvocatoria>\d+)/','docentes.views.descuentaCredito',name='descuentaCredito'),



	)