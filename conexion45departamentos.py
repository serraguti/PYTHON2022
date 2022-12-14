import pyodbc
servidor = "LOCALHOST"
bbdd = "HOSPITAL"
usuario = "SA"
password = ""

class ConexionDepartamentos:
    def __init__(self):
        # TENDREMOS LA CADENA DE CONEXION EN ESTE METODO
        # Y CREAMOS UNA PROPIEDAD LLAMADA conexion PARA
        # UTILIZARLA EN EL RESTO DE METODOS DE LA CLASE
        connectionString = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password
        # CREAMOS UNA PROPIEDAD LLAMADA conexion
        self.conexion = pyodbc.connect(connectionString)

    def insertarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO DEPT VALUES (?,?,?)"
        cursor.execute(sql, (numero, nombre, localidad))
        filasInsertadas = cursor.rowcount
        cursor.commit()
        cursor.close()
        return filasInsertadas
    
    def eliminarDepartamento(self, numero):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM DEPT WHERE DEPT_NO=?"
        cursor.execute(sql, (numero))
        filasEliminadas = cursor.rowcount
        cursor.commit()
        cursor.close()
        return filasEliminadas

    def modificarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sql = "UPDATE DEPT SET DNOMBRE=?, LOC=? WHERE DEPT_NO=?"
        cursor.execute(sql,(nombre, localidad, numero))
        filasModificadas = cursor.rowcount
        cursor.commit()
        cursor.close()
        return filasModificadas