from multiprocessing import context
from django.shortcuts import render, redirect
from principal.forms import *
from principal.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            messages.info(request,'Erro! Já existe um usuário com o mesmo e-mail')
            return render(request, 'cadastro.html')

    except User.DoesNotExist:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        storage = messages.get_messages(request)
        storage=True
        messages.info(request,'Usuário cadastrado com sucesso!')

        return render(request, 'cadastro.html')


def view_form_cadastro(request):
    return render(request, "cadastro.html")

@login_required
def index(request):
    produtos = Produto.objects.all()
    return render(request, "index.html", {'produtos': produtos})


def lista_produtos(request):
    #get produtos
    lista = Produto.objects.all()
    context = {'produtos': lista}
    return render(request, "produtos.html", context)

@login_required
def perfil_user_view(request):
    return render(request, 'perfil_user.html')
    


def quemsomos(request):
    return render(request, "quemsomos.html")

def tela_pedido (request):
    return render( request, 'pedido.html')
    
def tela_pagamento (request):
    return render( request, 'pagamento.html')

def detalhes(request, id):
    #get detalhes do produto
    produto = Produto.objects.get(id=id)
    context = {'produto': produto}
    return render(request, "detalhes.html", context)


# def cadastro_cliente(request):
#     #set infromações do cliente
#     form = Cliente_form(request.POST or None)

#     if request.method == "POST":
#         form =Cliente_form(request.POST) #Armazenando o formulário criado a uma lista
#         print(request.POST)
#         if form.is_valid():
#            form.save()
#         else:
#             form = Cliente_form()
        
#         form = Cliente_form()

#     return render(request, 'login.html', {'form': form })



def pesquisa(request):
   

    lista = Produto.objects.order_by("-id")
    if 'Pesquisa' in request.GET:
         lista = lista.filter(nome_produto__icontains=request.GET['Pesquisa'])


   
    print(lista)

    return render(request,'pagcategoria.html',{
        'produtos':lista,
    })
@login_required
def logout_aplicacao(request):
    logout(request)
    return redirect('login')