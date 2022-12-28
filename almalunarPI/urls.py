from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from principal.views import *
from django.conf import settings
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('catalogo/',lista_produtos.as_view(),name="produtos"),
    path('quemsomos/',quemsomos,name="quemsomos"),
    path('detalhes/<int:id>/',detalhes,name="detalhes"),
    path('pagcategoria', pesquisa, name="pagcategoria"),
    path('cadastro/', view_form_cadastro, name='cadastro'),
    path('cadastrar/', cadastrar_usuario, name="cadastrar"),
    path('accounts/login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('perfil/', perfil_user_view, name='perfil'),
    path('logout/', logout_aplicacao, name="logout"),
    path('carrinho/<int:id>/', add_carrinho, name='carrinho'),
    path('carrinho/', Comprar, name="carrinho"),
    path('remover_item/<int:id>', remover_pedido, name='remover_item'),
    path('pagamento/<int:id>/', tela_pagamento, name="pagamento"),
    path('cadastrar_endereco/', cadastro_adress, name='cadastro_adress'),
    path('remover_endereco/<int:id>', remover_adress, name='remover_adress'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)