from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import ItemVenda


@receiver(post_save, sender=ItemVenda)
def atualizar_total_venda(sender, instance, **kwargs):
    itens = instance.venda.itens.all()
    total = 0
    for item in itens:
        total += item.preco_unitario * item.quantidade
    instance.venda.total = total
    instance.venda.save()


@receiver(pre_delete, sender=ItemVenda)
def devolver_estoque(sender, instance, **kwargs):
    produto = instance.produto
    produto.estoque += instance.quantidade
    produto.save()
