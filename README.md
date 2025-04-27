# Sistema de Manipulação de Pedidos

Sistema desktop para gerenciar pedidos, extraindo dados de PDFs baixados de e-mails.

## Instalação
1. Clone o repositório: `git clone <url>`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale dependências: `pip install -r requirements.txt`
5. Copie `.env.example` para `.env` e configure as variáveis.
6. Execute: `python src/main.py`

## Configuração
- Configure as credenciais IMAP no `.env`.
- Certifique-se de que o SQLite está em `DB_PATH`.