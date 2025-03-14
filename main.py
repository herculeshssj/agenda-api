"""
    Programa principal, contendo os métodos REST da API.
"""
import db
import json
from fastapi import FastAPI
from model import NovaAgenda, EstadoAgenda, Agenda

app = FastAPI()

"""
    Apenas para conferir se a API está rodando de fato.
"""
@app.get("/ola-mundo")
def ola_mundo():
    return {"Ola": "Mundo"}


"""
    Lista as agendas cadastradas

    GET - /
"""
@app.get("/")
def consulta_agenda():
    agendas = db.buscar_agenda()
    resultado = []
    if agendas is not None:
        for agenda in agendas:
            dados = {
                "id": agenda[0],
                "titulo": agenda[1],
                "descricao": agenda[2],
                "dataInicio": agenda[3],
                "dataFim": agenda[4],
                "local": agenda[5],
                "estadoAtualAgenda": agenda[6]
            }
            resultado.append(dados)
            
    return resultado


"""
    Cadastra uma nova agenda

    POST - /
"""
@app.post("/")
def cadastra_agenda(novaAgenda: NovaAgenda):
    agenda = Agenda(id=0,
                    titulo=novaAgenda.titulo,
                    descricao=novaAgenda.descricao,
                    dataInicio=novaAgenda.dataInicio,
                    dataFim=novaAgenda.dataFim,
                    local=novaAgenda.local,
                    estadoAtualAgenda=EstadoAgenda.Recebido.value)

    db.cadastrar_agenda(agenda)
    return {"mensagem": "Agenda cadastrada com sucesso"}


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