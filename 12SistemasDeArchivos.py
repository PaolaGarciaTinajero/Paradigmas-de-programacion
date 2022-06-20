from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#===================================================
# Implementa la interface RepositorioDeUsuarios
#===================================================
class SistemaDeArchivos(RepositorioDeUsuarios):
    _directorio: str

    def _init_(mi, directorio:str):
        mi._directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi._directorio}")

    def guardar(mi, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivo _{mi._directorio}/{usuario.getNombre()}")
        print(xml)

    def cerrar(mi) -> None:
        print("Cerrando el archivo")

