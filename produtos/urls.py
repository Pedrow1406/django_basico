from django.urls import path, include
from . import views
urlpatterns = [
    path('ver/', views.ver, name='ver'),
    path('registrar_produto/', views.registrar_produto, name='registrar_produto'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
]
