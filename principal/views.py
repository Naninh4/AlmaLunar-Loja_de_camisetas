from multiprocessing import context
from django.shortcuts import render, redirect
from principal.forms import Adress_form
from django.shortcuts import redirect,get_object_or_404
from principal.models import Adress, Meu_usuario, Pedido, Produto
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView



# Create your views here.

@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            messages.info(request,'Erro! Esse email já está cadastrado.')
            return render(request, 'cadastro.html')

    except User.DoesNotExist:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpf = request.POST['cpf']
        new_user = User.objects.create_user(username=username, email=email, password=password) 
        new_user.save()
        new_myuser = Meu_usuario.objects.create( id_usuario = new_user.pk, cpf = cpf)
        new_myuser.save()
        storage = messages.get_messages(request)
        storage=True

        messages.info(request,'Usuário cadastrado com sucesso!')

        return render(request, 'cadastro.html')


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
    endereco = Adress.objects.filter(id_cliente = request.user.id)
    pedidos = Meu_usuario.objects.filter(id_usuario = request.user.id)
    usuario = User.objects.filter( id = request.user.id)
    return render(request, 'perfil_user.html',{'usuario':usuario, 'pedidos': pedidos, 'endereco': endereco})



def quemsomos(request):
    return render(request, "quemsomos.html")

@login_required
def tela_pagamento (request, id):
    endereco = Adress.objects.filter( id = id)
    pedidos = Pedido.objects.filter(id_cliente = request.user.id)
    valor = 0
    for x in pedidos:
        valor += x.valor_total
    
    return render( request,'pagamento.html',{'pedidos': pedidos, 'endereco': endereco, 'valor': valor} )

@login_required
def cadastro_adress(request):
    if request.method == 'POST':
        form = Adress_form(request.POST)
        if form.is_valid():
            form.instance.id_cliente = request.user.id
            form.save()
            return redirect('/perfil')
    else:
        form = Adress_form()

    print(form.errors)
    return render(request, 'cadastro_adress.html', {'form': form })

def detalhes(request, id):
    #get detalhes do produto
    produto = Produto.objects.get(pk=id)
    context = {'produto': produto}

    return render(request, "detalhes.html", context)

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


def Comprar(request):
    pedidos = Pedido.objects.filter(id_cliente = request.user.id )
    endereco = Adress.objects.filter( id_cliente = request.user.id)
    valor = 0
    for x in pedidos:
        valor += x.valor_total
    
    return render(request, 'carrinho.html', {'pedidos': pedidos, 'endereco': endereco , 'valor': valor})


@login_required
def add_carrinho(request,id):
    try:
        produto = Produto.objects.get(pk = id)
        pedido_aux = Pedido.objects.get(nome_produto = produto.nome_produto, id_cliente = request.user.id)

        if pedido_aux:
            messages.info(request,'Esse produto já foi adicionado ao carrinho!')
            return redirect('detalhes', produto.pk)

    except Pedido.DoesNotExist:
        produto = Produto.objects.get(pk = id)
        print(produto)
        new_pedido = Pedido( id_cliente = request.user.id, nome_produto = produto.nome_produto, valor_produto = produto.valor_produto, quantidade = request.POST['quantidade'] )
        print(new_pedido)
        new_pedido.save()
        print(produto)
        return redirect('detalhes', produto.pk)

@login_required
def remover_adress(request, id):
   adress_rm = Adress.objects.get( id = id)
   adress_rm.delete()
   return redirect('/perfil/')

@login_required
def remover_pedido(request, id):
   pedido_rm = Pedido.objects.get( id = id)
   pedido_rm.delete()
   return redirect('/carrinho/')
