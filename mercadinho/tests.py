from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import ItemVenda, Produto, Venda


class VendaTests(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome='Arroz',
            preco=10.00,
            estoque=5,
        )

    def test_criar_venda_atualiza_total_e_estoque(self):
        resposta = self.client.post(reverse('registrar_venda'), {
            'produto': self.produto.id,
            'quantidade': 2,
        })

        self.produto.refresh_from_db()
        venda = Venda.objects.first()
        venda.refresh_from_db()

        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(venda.total, Decimal('20.00'))
        self.assertEqual(self.produto.estoque, 3)

    def test_excluir_item_devolve_quantidade_ao_estoque(self):
        self.client.post(reverse('registrar_venda'), {
            'produto': self.produto.id,
            'quantidade': 2,
        })
        item = ItemVenda.objects.first()

        item.delete()

        self.produto.refresh_from_db()
        self.assertEqual(self.produto.estoque, 5)
