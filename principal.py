from conexion import DAO
import funciones
import os
import time
from funciones import barra_de_progreso
tiempo = 3

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar Mangas")
            print("2.- Registrar manga")
            print("3.- Actualizar manga")
            print("4.- Eliminar manga")
            print("5.- Exit")
            print("========================================================")
            print("")
            opcion = input("Seleccione una opción: ")
            if opcion >='1' or opcion <= '5':
                opcionCorrecta = True
                os.system("cls")
                ejecutarOpcion(opcion)
                




def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == '1':
        try:
            mangas = dao.listarMangas()
            if len(mangas) > 0:
                funciones.listarMangas(mangas)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == '2':
        completados = funciones.pedirDatosRegistro()
        try:
            dao.registrarManga(completados)
            print("Registrando Manga...")
            barra_de_progreso(tiempo)
            print("\nManga Registrado Con Exito!")
            time.sleep(1)
            os.system("cls")
        except:
            print("Ocurrió un error...")
    elif opcion == '3':
        try:
            mangas = dao.listarMangas()
            if len(mangas) > 0:
                completados = funciones.pedirDatosActualizacion(mangas)
                if completados:
                    dao.actualizarManga(completados) 
                    print("Actualizando Manga...")
                    barra_de_progreso(tiempo)
                    print("\nManga Actualizado Con Exito!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print("Nombre de manga a actualizar no encontrado...\n")
            else:
                print("No se encontraron mangas...")
        except:
            print("Ocurrió un error...")
    elif opcion == '4':
        try:
            mangas = dao.listarMangas()
            if len(mangas) > 0:
                nombreEliminar = funciones.pedirDatosEliminacion(mangas)
                if not(nombreEliminar == ""):
                    dao.eliminarManga(nombreEliminar)
                    print("Eliminando Manga...")
                    barra_de_progreso(tiempo)
                    print("\nManga Eliminado Con Exito!")
                    time.sleep(1)
                    os.system("cls")
                else:
                    print("Nombre de manga no encontrado...\n")
            else:
                print("No se encontraron mangas...")
        except:
            print("Ocurrió un error...")
    elif opcion == '5':
        exit()

    
    else:
        print("Opción no válida...")
        os.system("cls")
    

menuPrincipal()
