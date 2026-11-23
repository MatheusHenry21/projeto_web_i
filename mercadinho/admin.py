from django.contrib import admin

from .models import ItemVenda, Produto, Venda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 0
    readonly_fields = ('preco_unitario',)


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'criada_em', 'total')
    inlines = (ItemVendaInline,)
    readonly_fields = ('total',)

