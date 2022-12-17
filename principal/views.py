from multiprocessing import context
from django.shortcuts import render, redirect
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
    form = Cliente_form(request.POST or None)

    if request.method == "POST":
        form =Cliente_form(request.POST) #Armazenando o formulário criado a uma lista
        print(request.POST)
        if form.is_valid():
           form.save()
        else:
            form = Cliente_form()
        
        form = Cliente_form()

    return render(request, 'Login_Cadastro.html', {'form': form })



def pesquisa(request):
   

    lista = Produto.objects.order_by("-id")

    if 'categ' in request.GET:
        lista = lista.filter(categoria_produto_id=int(request.GET['categ']))
    if 'pesq' in request.GET:
         lista = lista.filter(nome_produto__icontains=request.GET['pesq'])


   
    print(lista)

    return render(request,'produtos.html',{
        'listap':lista,
    })
    