from django.contrib import admin
from .models import Produtos, Cliente
# Register your models here.

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin): ...

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin): ...
