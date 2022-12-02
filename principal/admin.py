from django.contrib import admin
from principal.models import Categoria, Produto, Cliente

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','nome_produto')

admin.site.register(Categoria)
admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente)