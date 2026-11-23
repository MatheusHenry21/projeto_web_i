from django.db import transaction

from . import repositories


def listar_produtos():
    return repositories.listar_produtos()


def listar_vendas():
    return repositories.listar_vendas()


def buscar_venda(venda_id):
    return repositories.buscar_venda(venda_id)


def registrar_venda(produto_id, quantidade):
    produto = repositories.buscar_produto(produto_id)
    if quantidade > produto.estoque:
        raise ValueError('Quantidade maior que o estoque disponível.')

    with transaction.atomic():
        venda = repositories.criar_venda()
        repositories.criar_item_venda(venda, produto, quantidade)
        repositories.baixar_estoque(produto, quantidade)

    return venda
