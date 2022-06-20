from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#============================
# Clase storemanager
# NO TIENE VARIABLES !!!
#============================
class ManejoDeInscripciones:
    #==========================================================
    # Decorador staticmethod
    # El objeto solo tiene la función inscribirUsuario
    # ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABÑES LOCALES
    # el objeto ManejoDeInscripciones es la interface intercambiable
    #==========================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario...\n")
        repositorioDeUsuario.abrir()
        repositorioDeUsuario.guardar(usuario)
        repositorioDeUsuario.cerrar()

