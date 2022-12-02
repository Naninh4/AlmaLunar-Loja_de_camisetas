from multiprocessing import context
from django.shortcuts import render
from principal.forms import Cliente_form
from principal.models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def lista_produtos(request):
    #get produtos
    lista = Produto.objects.all()
    context = {'produtos': lista}
    return render(request, "produtos.html", context)


def quemsomos(request):
    return render(request, "quemsomos.html")


def detalhes(request, id):
    #get detalhes do produto
    produto = Produto.objects.get(id=id)
    context = {'produto': produto}
    return render(request, "detalhes.html", context)


def cliente(request):
    #set infromações do cliente
    if request.method == 'POST':  # se o formulário for do tipo "post" ou seja, ele está sendo enviado como requisição
        form = Cliente_form(request.POST)
        form.save()  # salvando informações no banco de dados
        form = Cliente_form()  # CRIANDO UM FORMULÁRIO VAZIO
    else:
        form = Cliente_form

    return render(request, 'cadastro.html', {'form': form})
