from django.db import transaction

from .models import ItemVenda, Venda


def registrar_venda(produto, quantidade):
    if quantidade > produto.estoque:
        raise ValueError('Quantidade maior que o estoque disponível.')

    with transaction.atomic():
        venda = Venda.objects.create()
        item = ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco,
        )

        produto.estoque -= quantidade
        produto.save()

    return venda
