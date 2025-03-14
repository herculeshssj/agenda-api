"""
    Entidades utilizadas na API.
"""

from pydantic import BaseModel
from datetime import datetime

import enum

"""
    Classe Agenda, que representa a entidade Agenda na base de dados.
"""
class Agenda(BaseModel):
    id: int
    titulo: str
    descricao: str
    dataInicio: datetime
    dataFim: datetime
    local: str
    estadoAtualAgenda: str


"""
    Classe NovaAgenda, contendo os campos necessários para o cadastro de uma nova agenda.
"""
class NovaAgenda(BaseModel):
    titulo: str
    descricao: str
    dataInicio: datetime
    dataFim: datetime
    local: str

"""
    Enumerador que representa os estados possíveis de uma agenda.
"""
class EstadoAgenda(enum.Enum):
    Recebido = 'RECEBIDO'
    Confirmado = 'CONFIRMADO'
    Atendido = 'ATENDIDO'
    Cancelado = 'CANCELADO'