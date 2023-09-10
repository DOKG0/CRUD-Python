import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='',
                password='',
                db='mangas'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarMangas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM completados ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarManga(self, completados):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO completados (nombre, capitulos, tipo) VALUES ('{0}', {1}, '{2}')"
                cursor.execute(sql.format(completados[0], completados[1], completados[2]))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarManga(self, completados):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE completados SET capitulos = '{1}', tipo = '{2}' WHERE nombre = '{0}'"
                cursor.execute(sql.format (completados[0], completados[1], completados[2]))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def eliminarManga(self, codigoMangaEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM completados WHERE nombre = '{0}'"
                cursor.execute(sql.format(codigoMangaEliminar))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
