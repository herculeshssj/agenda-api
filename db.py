"""
    Métodos para conexão com a base SQlite.
"""

import sqlite3

from model import Agenda
from contextlib import closing
from datetime import datetime

"""
    Método para listar todos os registros da agenda.
"""
def buscar_agenda():
    with closing(sqlite3.connect('agenda.sqlite')) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM agenda')
        return cursor.fetchall()
    
"""
    Método para cadastrar uma nova agenda.
"""
def cadastrar_agenda(agenda: Agenda):
    with closing(sqlite3.connect('agenda.sqlite')) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO agenda (titulo, descricao, data_inicio, data_fim, local, estado_atual_agenda) VALUES (?, ?, ?, ?, ?, ?)', 
                       (agenda.titulo, 
                        agenda.descricao, 
                        datetime.strptime(str(agenda.dataInicio), '%Y-%m-%d %H:%M:%S'),
                        datetime.strptime(str(agenda.dataFim), '%Y-%m-%d %H:%M:%S'),
                        agenda.local, 
                        agenda.estadoAtualAgenda))
        conn.commit()


"""
    Método para atualizar uma agenda.
"""
def atualizar_agenda(agenda: Agenda):
    with closing(sqlite3.connect('agenda.sqlite')) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE agenda SET titulo = ?, descricao = ?, data_inicio = ?, data_fim = ?, local = ? WHERE id = ?', 
                       (agenda.titulo, 
                        agenda.descricao, 
                        datetime.strptime(str(agenda.dataInicio), '%Y-%m-%d %H:%M:%S'),
                        datetime.strptime(str(agenda.dataFim), '%Y-%m-%d %H:%M:%S'),
                        agenda.local, 
                        agenda.id))
        conn.commit()


"""
    Método para deletar uma agenda.
"""
def deletar_agenda(id: int):
    with closing(sqlite3.connect('agenda.sqlite')) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM agenda WHERE id = ?', (id,))
        conn.commit()


"""
    Método para atualizar o status de uma agenda.
"""
def atualizar_status_agenda(id: int, status: str):
    with closing(sqlite3.connect('agenda.sqlite')) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE agenda SET estado_atual_agenda = ? WHERE id = ?', (status, id))
        conn.commit()