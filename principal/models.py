from distutils.command.upload import upload
from django.db import models
# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor_produto = models.DecimalField('Preço do Produto',max_digits=8,decimal_places=2)
    imagem_produto = models.ImageField(upload_to='produtos/',blank=True,null=True,max_length=250)
    descricao_produto = models.TextField()
    categoria_produto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # qnt_disponivel = models.IntegerField()

    def __str__(self):
        return self.nome_produto



class Cliente(models.Model):
    nome_cliente  = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    senha_cliente = models.CharField(max_length=8,blank=False)


class endereco (models.Model):
    pais = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    
    def __str__(self):
        return "Rua: {},N° {}, {}, {}, {}, {}".format(self.rua, self.numero, self.bairro, self.cidade, self.estado, self.pais)
    
