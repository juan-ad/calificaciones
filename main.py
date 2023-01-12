from crud import *
from conn import connection

menu = """
------------------------------------------------------
 Bienvenido al registro de calificaciones, eliga una 
 de las siguientes opciones:

 [1] Ingresar Calificación
 [2] Actualizar Calificación
 [3] Listar Estudiantes
 [4] Eliminar estudiante
 [5] Salir
-------------------------------------------------------
"""

def main():
    conn = connection()
    print(menu)
    opcion = int(input('Digite una opción: '))
    print("\n")
    while(opcion != 5):
        
        if (opcion == 1):
            print("***************** Ingresar un nuevo estudiante ******************\n")
            nombre = input("Digite el nombre del estudiante: ")
            apellido = input("Digite el apellido del estudiante: ")
            asignatura = input("Digite la asignatura del estudiante: ")
            calificacion = input("Digite la calificación del estudiante: ")
            estudiante = (nombre, apellido, asignatura, calificacion)
            print("\n")
            create(conn, estudiante)
            print("")
            print("*****************************************************************\n")
        elif (opcion == 2):
            print("***************** Actualizar un estudiante ******************\n")
            id = input("Digite el id del estudiante a modificar: ")
            nombre = input("Digite el nombre del estudiante: ")
            apellido = input("Digite el apellido del estudiante: ")
            asignatura = input("Digite la asignatura del estudiante: ")
            calificacion = input("Digite la calificación del estudiante: ")
            estudiante = (nombre, apellido, asignatura, calificacion, id)
            print("\n")
            update(conn, estudiante)
            print("")
            print("*****************************************************************\n")
        elif (opcion == 3):
            read(conn)
        elif (opcion == 4):
            print("***************** Eliminar un estudiante ******************\n")
            id = input("Digite el id del estudiante a eliminar: ")
            print("")
            delete(conn, (id))
            print("")
            print("*****************************************************************\n")
        else: 
            print("¡Opción Incorrecta!\n")
        opcion = int(input('Digite una opción: '))
        print("\n")
    conn.close()
    print("Adiós !!!")
if __name__ == '__main__':
    main()