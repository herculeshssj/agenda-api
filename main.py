"""
    Programa principal, contendo os métodos REST da API.
"""

from fastapi import FastAPI

app = FastAPI()

"""
    Apenas para conferir se a API está rodando de fato.
"""
@app.get("/ola-mundo")
def ola_mundo():
    return {"Ola": "Mundo"}


"""
    GET - /
"""
def consulta_agenda():
    pass

"""
    POST - /
"""
def cadastra_agenda():
    pass

"""
    PUT - /{id}
"""
def atualiza_agenda():
    pass


"""
    DELETE - /{id}
"""
def exclui_agenda():
    pass


"""
    PATCH - /{id}/{status}
"""
def atualiza_status_agenda():
    pass