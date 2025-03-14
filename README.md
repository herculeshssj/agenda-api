# agenda-api
API REST para gestão de agenda de compromissos.

## Configuração do ambiente de desenvolvimento

**Requisitos:**
- Python 3.11 ou superior;
- IDE com suporte a Python (Pycharm, VSCode, etc).

**Virtualenv**

Faça o clone do repositório:

```sh
git clone https://github.com/herculeshssj/agenda-api.git
```

Dentro da pasta **agenda-api**, crie um novo ambiente virtual:

```sh
python -m venv venv
```

Ative o ambiente virtual:

```sh
source venv/bin/activate
```

Faça a instalação das dependências:

```sh
pip install -r requirements.txt
```

Para executar a API:

```sh
uvicorn main:app --reload
```

A API estará acessível no endereço http://127.0.0.1/8000. A lista completa de endpoints está disponível em http://127.0.0.1/8000/docs.