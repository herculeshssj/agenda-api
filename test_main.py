"""
    Testes unitários para a API da agenda.
"""

import pytest
from fastapi.testclient import TestClient
from main import app
from model import AgendaVO, EstadoAgenda


client = TestClient(app)

"""
    Teste para o método de consulta de agenda, endpoint GET /.
"""
def test_consulta_agenda(monkeypatch):
    def mock_buscar_agenda():
        return [
            (1, "Titulo 1", "Descricao 1", "2023-01-01", "2023-01-02", "Local 1", "Recebido"),
            (2, "Titulo 2", "Descricao 2", "2023-02-01", "2023-02-02", "Local 2", "Confirmado")
        ]
    monkeypatch.setattr("db.buscar_agenda", mock_buscar_agenda)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "titulo": "Titulo 1", "descricao": "Descricao 1", "dataInicio": "2023-01-01", "dataFim": "2023-01-02", "local": "Local 1", "estadoAtualAgenda": "Recebido"},
        {"id": 2, "titulo": "Titulo 2", "descricao": "Descricao 2", "dataInicio": "2023-02-01", "dataFim": "2023-02-02", "local": "Local 2", "estadoAtualAgenda": "Confirmado"}
    ]

"""
    Teste para o método de cadastro de agenda, endpoint POST /."
"""
def test_cadastra_agenda(monkeypatch):
    def mock_cadastrar_agenda(agenda):
        return None
    monkeypatch.setattr("db.cadastrar_agenda", mock_cadastrar_agenda)
    nova_agenda = {
        "titulo": "Titulo 3",
        "descricao": "Descricao 3",
        "dataInicio": "2023-03-01",
        "dataFim": "2023-03-02",
        "local": "Local 3"
    }
    response = client.post("/", json=nova_agenda)
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Agenda cadastrada com sucesso"}


"""
    Teste para o método de atualização de agenda, endpoint PUT /{id}.
""" 
def test_atualiza_agenda(monkeypatch):
    def mock_atualizar_agenda(agenda):
        return None
    monkeypatch.setattr("db.atualizar_agenda", mock_atualizar_agenda)
    agenda_atualizada = {
        "titulo": "Titulo Atualizado",
        "descricao": "Descricao Atualizada",
        "dataInicio": "2023-04-01",
        "dataFim": "2023-04-02",
        "local": "Local Atualizado"
    }
    response = client.put("/1", json=agenda_atualizada)
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Agenda atualizada com sucesso"}


"""
    Teste para o método de exclusão de agenda, endpoint DELETE /{id}.
"""
def test_exclui_agenda(monkeypatch):
    def mock_deletar_agenda(id):
        return None
    monkeypatch.setattr("db.deletar_agenda", mock_deletar_agenda)
    response = client.delete("/1")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Agenda excluída com sucesso"}


""""
    Teste para o método de atualização de status de agenda, endpoint PATCH /{id}/{status}.
"""
def test_atualiza_status_agenda(monkeypatch):
    def mock_atualizar_status_agenda(id, status):
        return None
    monkeypatch.setattr("db.atualizar_status_agenda", mock_atualizar_status_agenda)
    response = client.patch("/1/confirmado")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Status da agenda atualizado com sucesso"}

    response = client.patch("/1/invalid_status")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Status inválido"}