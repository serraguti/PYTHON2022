# UTILIZAMOS EXPLICITAMENTE PYODBC??
# QUE CLASE UTILIZA LOS CURSORES Y LAS CONSULTAS SQL??
from conexion44enfermos import ConexionEnfermos

# CREAMOS UN OBJETO DE LA CLASE CONEXIONENFERMOS
connection = ConexionEnfermos()
print("Escriba una inscripción para eliminar")
inscripcion = input()
# LA CLASE CONEXION NOS DEVUELVE EL NUMERO DE ENFERMOS
# ELIMINADOS
respuesta = connection.eliminarEnfermo(inscripcion)
print("Enfermos eliminados: " + str(respuesta))
print("Fin de programa")
