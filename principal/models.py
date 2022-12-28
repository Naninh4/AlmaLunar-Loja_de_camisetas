from distutils.command.upload import upload
from django.db import models
from django.conf import settings
import decimal
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

    def __str__(self):
        return self.nome_produto

    
class Adress (models.Model):
    id_cliente = models.IntegerField()
    pais = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField()
    
    def __str__(self):
        return "Rua: {},N° {}, {}, {}, {}, {}".format(self.rua, self.numero, self.bairro, self.cidade, self.estado, self.pais)
class Pedido (models.Model):
    id_cliente = models.IntegerField()
    nome_produto = models.CharField(max_length=250 )
    valor_produto = models.FloatField(default=0.0)
    quantidade = models.IntegerField(default=0)
    valor_total = models.FloatField(default=0.0)

    def save(self,*args, **kwargs):
        self.valor_total = self.valor_produto * decimal.Decimal(self.quantidade)
        super(Pedido, self).save(*args, **kwargs)
    
class Meu_usuario(models.Model):
    id_usuario = models.IntegerField()
    cpf = models.CharField( max_length=11, blank=True)