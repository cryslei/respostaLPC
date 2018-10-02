from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('clientes/', clientes, name='lista-clientes'),
    path('clientes/estatisticas/', clientes_estatisticas, name='lista-clientes-estatisticas'),
]
