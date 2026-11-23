from django.shortcuts import get_object_or_404, redirect, render

from .forms import ItemVendaForm
from .models import ItemVenda, Produto, Venda


def inicio(request):
    produtos = Produto.objects.all()
    return render(request, 'mercadinho/inicio.html', {'produtos': produtos})


def registrar_venda(request):
    if request.method == 'POST':
        form = ItemVendaForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            if item.quantidade <= item.produto.estoque:
                item.venda = Venda.objects.create()
                item.preco_unitario = item.produto.preco
                item.save()
                item.produto.estoque -= item.quantidade
                item.produto.save()
                item.venda.total = item.preco_unitario * item.quantidade
                item.venda.save()
                return redirect('detalhe_venda', venda_id=item.venda.id)
            form.add_error('quantidade', 'Quantidade maior que o estoque disponível.')
    else:
        form = ItemVendaForm()
    return render(request, 'mercadinho/nova_venda.html', {'form': form})


def historico_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'mercadinho/historico.html', {'vendas': vendas})


def detalhe_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    return render(request, 'mercadinho/detalhe_venda.html', {'venda': venda})

