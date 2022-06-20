from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#===================================================
# S3 es hijo de RepositorioDeUsuarios
#===================================================
class S3(RepositoriosDeUsuarios):
    _clientId: str
    _secretKey: str
    _bucket: str

    def _init_(mi, clientId: str, secretKey: str, bucket: str):
        mi._clientId = cliendIt
        mi._secretKey = secretKey
        mi._bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi._clienteId}:
        {mi._secretKey}")

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(), 
                "apellido": usuario.getApellido(), 
                "edad": usuario.getEdad()}
        print(f"Guardando usuario de la bandeja:{mi._bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando conexión AWS S3")

