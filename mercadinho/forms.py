from django import forms

from .models import ItemVenda, Produto


class ItemVendaForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail para confirmação', required=False)

    class Meta:
        model = ItemVenda
        fields = ('produto', 'quantidade')
        widgets = {
            'produto': forms.Select(attrs={'class': 'campo'}),
            'quantidade': forms.NumberInput(attrs={'class': 'campo', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(ativo=True, estoque__gt=0)

