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

_Linux_

```sh
source venv/bin/activate
```

_Windows_

```sh
.\venv\Scripts\Activate.ps1
```

*Obs:* No Windows é necessário permitir a execução de scripts PowerShell. Habilite rodando em um terminal PowerShell como administrador:

```sh
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
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

## Deploy em produção

**Requisitos**
- Docker

**Construção da imagem**

Para construir a imagem Docker:

```sh
docker build -t agenda-api:latest .
```

Copie o arquivo **agenda.sqlite** para o diretório do seu usuário.

Para executar o container Docker:

```sh
docker run --name agenda-api -p 8000:8000 -v ~/agenda.sqlite:/usr/src/app/agenda.sqlite -d agenda-api:latest
```