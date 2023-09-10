import time
import sys

def barra_de_progreso(segundos):
    for i in range(segundos):
        time.sleep(1)  # Espera 1 segundo
        progreso = i * 40 // segundos  # Calcula el progreso proporcional
        barra = "[" + "#" * progreso + " " * (40 - progreso) + "]"  # Crea la barra de progreso
        sys.stdout.write("\r" + barra)  # Actualiza la barra de progreso en la misma línea
        sys.stdout.flush()

def listarMangas(mangas):
    print("Mangas: \n")
    contador = 1
    for man in mangas:
        datos = "{0}. Nombre: {1} | Capitulos: {2} | Tipo: {3}"
        print(datos.format(contador, man[0], man[1], man[2]))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    nombreCorrecto = False
    while(not nombreCorrecto):
        nombre = input("Ingrese nombre: ")
        if len(nombre) > 0:
            nombreCorrecto = True
        else:
            print("Nombre incorrecto: Debe tener mas de 0 letras.")


    capitulosCorrecto = False
    while(not capitulosCorrecto):
        capitulos = input("Ingrese capitulos: ")
        if capitulos.isnumeric():
            if (int(capitulos) > 0):
                capitulosCorrecto = True
                capitulos = int(capitulos)
            else:
                print("Los capitulos ingresados deben ser mayor a 0.")
        else:
            print("Capitulos incorrectos: Debe ser un número únicamente.")
            
    tipo = input("Ingrese tipo: ")

    completados = (nombre, capitulos, tipo)
    return completados

def pedirDatosActualizacion(mangas):
    listarMangas(mangas)
    nombreEditar = input("Ingrese el nombre del manga a editar: ")

    for manga in mangas:
        if manga[0] == nombreEditar:
            capitulos = input("Ingrese nuevos capítulos (deje en blanco para no cambiar): ")
            tipo = input("Ingrese nuevo tipo (deje en blanco para no cambiar): ")

            if capitulos.strip() == "":
                capitulos = manga[1]
            if tipo.strip() == "":
                tipo = manga[2]

            while not capitulos.isdigit() or int(capitulos) <= 0:
                print("Capítulos incorrectos. Debe ser un número mayor que 0.")
                capitulos = input("Ingrese nuevos capítulos (deje en blanco para no cambiar): ")

            completados = (manga[0], int(capitulos), tipo, nombreEditar)
            return completados
            

    #print("Nombre de manga a actualizar no encontrado...")
    return None

def pedirDatosEliminacion(mangas):
    listarMangas(mangas)
    existeNombre = False
    nombreEliminar = input("Ingrese el nombre del manga a eliminar: ")
    for man in mangas:
        if man[0] == nombreEliminar:
            existeNombre = True
            break

    if not existeNombre:
        nombreEliminar = ""

    return nombreEliminar
