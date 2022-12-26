from multiprocessing import context
from django.shortcuts import render, redirect
from principal.forms import *
from django.shortcuts import redirect,get_object_or_404
from principal.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


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

@login_required
def update_senha(UpdateView):
    Template_name= 'cadastro.html'
    model = User
    fields = ['password']
    success_url = 'index.html'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(User, usuario=self.request.user)
        return self.object


@login_required

class Carrinho(ListView):
    model = Pedido
    template_name = "carrinho.html"

def view_form_cadastro(request):
    return render(request, "cadastro.html")

def index(request):
    produtos = Produto.objects.all()
    return render(request, "index.html", {'produtos': produtos})


class lista_produtos(ListView):
    #get produtos
    model = Produto
    template_name = 'produtos.html'

@login_required
def perfil_user_view(request):
    usuario = User.objects.filter( id = request.user.id)
    return render(request, 'perfil_user.html', {'usuario':usuario})


def quemsomos(request):
    return render(request, "quemsomos.html")




# def cal(request):
#     quantidade = request.POST['quantidade']
#     context = quantidade * Produto.valor_produto
#     return render(request, 'pedido.html',context)

@login_required
def tela_pagamento (request):
    return render( request, 'pagamento.html')

def detalhes(request, id):
    #get detalhes do produto
    produto = Produto.objects.get(pk=id)
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

@login_required
def Comprar(request):
    pedidos = Pedido.objects.filter(id_cliente = request.user.id )
    return render(request, 'carrinho.html', {'pedidos': pedidos})
@login_required
def add_carrinho(request,id):
    # usuario = User.objects.get(username = request.user)
    try:
        produto = Produto.objects.get(pk = id)
        pedido_aux = Pedido.objects.get(nome_produto= produto.nome_produto)

        if pedido_aux:
            messages.info(request,'Erro! Já existe um usuário com o mesmo e-mail')
            return redirect('detalhes', produto.pk)

    except Pedido.DoesNotExist:
        produto = Produto.objects.get(pk = id)
        print(produto)
        new_pedido = Pedido( id_cliente = request.user.id, nome_produto = produto.nome_produto, valor_produto = produto.valor_produto, quantidade = request.POST['quantidade'] )
        print(new_pedido)
        new_pedido.save()
        print(produto)
        return redirect('detalhes', produto.pk)