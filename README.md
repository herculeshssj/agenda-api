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

**Dependências**

Faça a instalação das dependências:

```sh
pip install -r requirements.txt
```

**Base de dados**

O projeto acompanha uma base SQlite com a tabela já criada. Segue abaixo o esquema da tabela:

```sql
create table agenda(
    id integer primary key,
    titulo text not null,
    descricao text null,
    data_inicio text not null,
    data_fim text null,
    local text null,
    estado_atual_agenda text not null
);
```

Os valores dos campos 'data_inicio' e 'data_fim' são salvos no formato 'YYYY-MM-DD HH:MM:SS'.

**Execução**

Para executar a API:

```sh
uvicorn main:app --reload
```

A API estará acessível no endereço http://127.0.0.1/8000. A lista completa de endpoints está disponível em http://127.0.0.1/8000/docs.

**Testes**

Para rodar os testes unitários, é necessário a API estar em execução.

Para executar os testes:

```sh
pytest test_main.py
```