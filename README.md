# Mercadinho

Projeto acadêmico simples de vendas de mercadinho, feito com Django e PostgreSQL. Ele serve de exemplo para estudar recursos e padrões do framework.

## O que o projeto demonstra

- **Django Signals** — em `mercadinho/signals.py`, `post_save` recalcula o total da venda quando um item é salvo; `pre_delete` devolve ao estoque a quantidade do item excluído.
- **Middlewares customizados** — `RegistrarAcessoMiddleware` conta os acessos na sessão; `CabecalhoLojaMiddleware` adiciona o cabeçalho `X-Mercadinho` à resposta.
- **Service Layer / Use Case** — `services.registrar_venda()` representa o caso de uso de registrar uma venda: confere o estoque e coordena a criação da venda e do item.
- **Repository** — `repositories.py` concentra consultas e gravações no banco. O serviço usa o repositório; a view cuida do formulário e da resposta HTTP.
- **E-mail** — a view chama `send_mail` se um e-mail for informado. No ambiente local, a mensagem aparece no terminal usando o backend de console.
- **Testes** — `mercadinho/tests.py` contém dois testes: registro de venda com atualização do total e do estoque, e devolução ao estoque ao excluir um item.
- **i18n e l10n** — na página de produtos, `{% translate %}` marca um texto para tradução e `|localize` formata o preço conforme a localidade.

Uma venda deste exemplo contém um produto. O cadastro de produtos é feito pelo Django Admin.

## Preparar para executar localmente

É necessário ter Python e PostgreSQL instalados.

1. Crie e ative um ambiente virtual:

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Instale as dependências e crie o arquivo local de configuração:

   ```powershell
   pip install -r requirements.txt
   Copy-Item .env.example .env
   ```

3. Edite `.env` com os dados do seu PostgreSQL e substitua `SECRET_KEY` por uma chave gerada com:

   ```powershell
   py -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

4. Prepare o banco e carregue produtos de exemplo:

   ```powershell
   py manage.py migrate
   py manage.py loaddata produtos
   py manage.py createsuperuser
   ```

5. Inicie o projeto:

   ```powershell
   py manage.py runserver
   ```

Abra `http://127.0.0.1:8000/` para ver os produtos. O cadastro e a administração ficam em `http://127.0.0.1:8000/admin/`.

## Executar os testes

```powershell
py manage.py test mercadinho
```

## Render

O arquivo `render.yaml` define um serviço Django e um PostgreSQL no Render. Para usá-lo, envie o projeto para o GitHub, crie um Blueprint no Render apontando para o repositório e aplique a configuração. O Render instala as dependências, prepara os arquivos estáticos, compila as traduções e aplica as migrações durante o build.

O arquivo `.env` contém configurações locais e não deve ser enviado ao Git. No Render, a chave secreta e a conexão com o banco são fornecidas pela própria configuração do Blueprint.
