from django.shortcuts import get_object_or_404, redirect, render

from .forms import ItemVendaForm
from .models import Produto, Venda
from .services import registrar_venda as criar_venda


def inicio(request):
    produtos = Produto.objects.all()
    return render(request, 'mercadinho/inicio.html', {'produtos': produtos})


def registrar_venda(request):
    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']
            try:
                venda = criar_venda(produto, quantidade)
                return redirect('detalhe_venda', venda_id=venda.id)
            except ValueError as erro:
                form.add_error('quantidade', str(erro))
    else:
        form = ItemVendaForm()
    return render(request, 'mercadinho/nova_venda.html', {'form': form})


def historico_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'mercadinho/historico.html', {'vendas': vendas})


def detalhe_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    return render(request, 'mercadinho/detalhe_venda.html', {'venda': venda})

