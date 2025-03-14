"""
    Métodos para conexão com a base SQlite.
"""

import sqlite3

from contextlib import closing

"""
    Método para listar todos os registros da agenda.
"""
def buscar_agenda():
    with closing(sqlite3.connect('agenda.sqlite')) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM agenda')
        return cursor.fetchall()