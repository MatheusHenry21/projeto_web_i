from django.http import Http404
from django.shortcuts import redirect, render

from .forms import ItemVendaForm
from .services import (
    buscar_venda,
    listar_produtos,
    listar_vendas,
    registrar_venda as criar_venda,
)


def inicio(request):
    produtos = listar_produtos()
    return render(request, 'mercadinho/inicio.html', {'produtos': produtos})


def registrar_venda(request):
    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']
            try:
                venda = criar_venda(produto.id, quantidade)
                return redirect('detalhe_venda', venda_id=venda.id)
            except ValueError as erro:
                form.add_error('quantidade', str(erro))
    else:
        form = ItemVendaForm()
    return render(request, 'mercadinho/nova_venda.html', {'form': form})


def historico_vendas(request):
    vendas = listar_vendas()
    return render(request, 'mercadinho/historico.html', {'vendas': vendas})


def detalhe_venda(request, venda_id):
    venda = buscar_venda(venda_id)
    if venda is None:
        raise Http404('Venda não encontrada.')
    return render(request, 'mercadinho/detalhe_venda.html', {'venda': venda})

