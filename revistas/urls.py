from django.conf.urls import  *

from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),


    url(r'^inicioRevistas/','revistas.views.inicioRevistas',name='inicioRevistas'),



	)