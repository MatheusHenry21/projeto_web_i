from .models import ItemVenda, Produto, Venda


def listar_produtos():
    return Produto.objects.all()


def buscar_produto(produto_id):
    return Produto.objects.get(pk=produto_id)


def listar_vendas():
    return Venda.objects.all()


def buscar_venda(venda_id):
    return Venda.objects.filter(pk=venda_id).first()


def criar_venda():
    return Venda.objects.create()


def criar_item_venda(venda, produto, quantidade):
    return ItemVenda.objects.create(
        venda=venda,
        produto=produto,
        quantidade=quantidade,
        preco_unitario=produto.preco,
    )


def baixar_estoque(produto, quantidade):
    produto.estoque -= quantidade
    produto.save()
