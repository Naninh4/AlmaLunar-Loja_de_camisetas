from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from principal.views import *
from django.conf import settings
from principal.models import * 
from principal.forms import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('lista/',lista_produtos,name="produtos"),
    path('quemsomos/',quemsomos,name="quemsomos"),
    path('detalhes',detalhes,name="detalhes"),
    path('detalhes/<int:id>',detalhes,name="detalhes"),
    path('form/',cliente, name="L_G")

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)