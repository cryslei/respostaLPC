from django.shortcuts import render
from .models import *

# Create your views here.
def orcamentos_lista(request):
    # logica
    orcamentos = Orcamento.objects.all()
    return render(request, 'mp_orcamento/orcamentos.html', {'orcamentos': orcamentos})


def orcamentos_estatisticas(request):
    maior_custo = 0
    menor_custo = 999999999999
    orcamento_maior_custo = None
    orcamento_menor_custo = None
    orcamentos = Orcamento.objects.all()
    somatorio_custo_total = 0
    for orcamento in orcamentos:
        somatorio = 0
        for peca in Peca.objects.filter(orcamento=orcamento):
            somatorio += peca.custo_de_producao_ajustado()
        orcamento.custo_total = somatorio * 1.25
        somatorio_custo_total += orcamento.custo_total
        if orcamento.custo_total >= maior_custo:
            orcamento_maior_custo = orcamento
            maior_custo = orcamento.custo_total
        if orcamento.custo_total <= menor_custo:
            orcamento_menor_custo = orcamento
            menor_custo = orcamento.custo_total
    quantidade = Orcamento.objects.count() 
    
    media_custo_total = somatorio_custo_total / quantidade
    return render(request, 'mp_orcamento/estatisticas.html', 
        {'quantidade': quantidade, 
        'orcamento_maior_custo': orcamento_maior_custo,
        'orcamento_menor_custo': orcamento_menor_custo,
        'media_custo_total': media_custo_total,
        
        })
def clientes(request):
    cliente = Cliente.objects.count()
    orcamentos = Orcamento.objects.all()
    nome = orcamentos[0].cliente.nome
    email = orcamentos[0].cliente.email
    lista_data = list()
    lista_custo = list()
    for i in orcamentos:
        if nome == i.cliente.nome:
            lista_data.append(i.data_hora)
            lista_custo.append(i.custo_total)
            
    return render(request,'clientes/lista-clientes.html', {'nome': nome,'cliente': cliente,'email':email,'lista_data':lista_data,'lista_custo':lista_custo})
def clientes_estatisticas(request):
    maior_custo = 0
    menor_custo = 999999999999
    cliente_maior_custo = None
    cliente_menor_custo = None
    orcamentos = Orcamento.objects.all()
    somatorio_custo_total = 0
    for orcamento in orcamentos:
        somatorio = 0
        for peca in Peca.objects.filter(orcamento=orcamento):
            somatorio += peca.custo_de_producao_ajustado()
        orcamento.custo_total = somatorio * 1.25
        somatorio_custo_total += orcamento.custo_total
        if orcamento.custo_total >= maior_custo:
            cliente_maior_custo = orcamento
            maior_custo = orcamento.custo_total
        if orcamento.custo_total <= menor_custo:
            cliente_menor_custo = orcamento
            menor_custo = orcamento.custo_total
    cliente = Cliente.objects.count()
    return render(request, 'clientes/estatisticas.html', 
        {'cliente_maior_custo': cliente_maior_custo,
        'cliente_menor_custo': cliente_menor_custo,
        'cliente': cliente
        })
    
