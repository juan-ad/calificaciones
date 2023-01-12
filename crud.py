from sqlite3 import Error

def read(conn):
    cursor = conn.cursor()
    try:
        query = cursor.execute("SELECT * FROM estudiante")
        estudiantes = query.fetchall()
        print("********************** Listado de Estudiantes **********************\n")
        for estudiante in estudiantes:
            print(f'Id: {estudiante[0]} Nombre: {estudiante[1]} {estudiante[2]} Asignatura: {estudiante[3]} Calificacion: {estudiante[4]} ')
        print("")    
        print("********************************************************************\n")
        conn.commit()
    except:
        print("Error al listar")

def create(conn, estudiante):
    cursor = conn.cursor()
    sql = '''
        INSERT INTO estudiante(nom_estudiante, ape_estudiante, asignatura, calificacion) 
        VALUES(?,?,?,?)
    '''
    try:
        cursor.execute(sql, estudiante)
        print("Estudiante registrado con éxito")
        conn.commit()
    except:
        print("Estudiante no se pudo registrar")


def update(conn, estudiante):
    cursor = conn.cursor()
    sql = '''
        UPDATE estudiante SET nom_estudiante=?, ape_estudiante=?, asignatura=?, calificacion=?
        WHERE id = ? 

    '''
    try:
        cursor.execute(sql, estudiante)
        print("Estudiante actualizado con éxito")
        conn.commit()
    except:
        print("No se pudo actualizar el estudiante")

def delete(conn, id):
    cursor = conn.cursor()
    try:
        cursor.execute(f'DELETE FROM estudiante WHERE id = {id}')
        print("Estudiante eliminado satisfactoriamente")
        conn.commit()
    except Error as e: 
        print(e)
        print("Error: no existe un estudiante con ese id")


