from django.contrib import admin
from principal.models import *

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','nome_produto')

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('id','nome_categoria')

admin.site.register(Categoria)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Adress)
admin.site.register(Pedido)

