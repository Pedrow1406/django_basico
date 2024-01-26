from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produtos, Cliente
# Create your views here.

def ver_compras(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        clientes = Cliente.objects.all()
        return render(request, 'cliente/ver_compras.html', {'clientes': clientes, 'status':status})
    elif request.method == 'POST':
        nome_cliente = request.POST.get('nome')
        cliente = Cliente.objects.get(nome_cliente = nome_cliente)
        produto = Produtos.objects.filter(cliente_id = cliente.id)
        clientes = Cliente.objects.all()
        return  render(request, 'cliente/ver_compras.html', {'clientes':clientes,'produtos': produto, 'status': '1', 'nome_cliente':nome_cliente})
    
def registrar_produto(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        cliente = Cliente.objects.all()
        return render(request, 'produtos/registrar_produto.html', {'status':status, 'clientes':cliente})
    elif request.method == 'POST':
        nome_produto = request.POST.get('nome')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        nome_cliente = request.POST.get('cliente')
        cliente = Cliente.objects.get(nome_cliente=nome_cliente)
        produto = Produtos(
            nome = nome_produto,
            preco = preco,
            quantidade = quantidade,
            cliente = cliente
        )
        produto.save()
        return redirect('/produtos/registrar_produto/?status=1')
    
def registrar_cliente(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cliente/registrar_cliente.html', {'status':status})
    elif request.method == 'POST':
        nome_cliente = request.POST.get('nome_cliente')
        idade_cliente = request.POST.get('idade')
        idade_cliente = int(idade_cliente)
        if idade_cliente < 18:
            return render(request, 'cliente/registrar_cliente.html', {'idade_cliente': 'menor_idade'})
        if idade_cliente > 100:
            return render(request, 'cliente/registrar_cliente.html', {'idade_cliente': 'idade_invalida'})
        cliente = Cliente(
            nome_cliente = nome_cliente,
            idade_cliente = idade_cliente
        )
        cliente.save()
        return redirect('/produtos/registrar_cliente/?status=1')