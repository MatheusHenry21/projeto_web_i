from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vendas/nova/', views.registrar_venda, name='registrar_venda'),
    path('vendas/', views.historico_vendas, name='historico_vendas'),
    path('vendas/<int:venda_id>/', views.detalhe_venda, name='detalhe_venda'),
]

