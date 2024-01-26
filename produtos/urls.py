from django.urls import path, include
from . import views
urlpatterns = [
    path('registrar_produto/', views.registrar_produto, name='registrar_produto'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('ver_compras/', views.ver_compras, name='ver_compras'),
]
