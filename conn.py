import sqlite3
from sqlite3 import Error

def create_database():
    db = sqlite3.connect('calificaciones.db')
    db.execute('''
        CREATE TABLE estudiante(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_estudiante VARCHAR(50),
            ape_estudiante VARCHAR(50),
            asignatura VARCHAR(50),
            calificacion DOUBLE 
        )
    ''')

def connection():
    conn = None
    try:
        conn = sqlite3.connect('calificaciones.db')
    except Error as e:
        print(e)
    
    return conn
