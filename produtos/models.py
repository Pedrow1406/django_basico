from django.db import models
# Create your models here.


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=50)
    idade_cliente = models.IntegerField()
    
    def __str__(self):
        return self.nome_cliente


class Produtos(models.Model):
    nome = models.CharField(max_length=40)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome