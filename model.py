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
    Enumerador que representa os estados possíveis de uma agenda.
"""
class EstadoAgenda(enum.Enum):
    Recebido = 'RECEBIDO'
    Confirmado = 'CONFIRMADO'
    Atendido = 'ATENDIDO'
    Cancelado = 'CANCELADO'