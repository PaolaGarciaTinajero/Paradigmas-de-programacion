#=================
# Clase Usuario
#=================
class Usuario:
    _nombre: str
    _apellido: str
    _edad: str

    #====================
    # Constructor
    #====================
    def _init_(mi, nombre: str, apellido:str, edad:str):
        mi._nombre = nombre
        mi._apellido = apellido
        mi._edad = edad

    #====================
    # Getters 
    #===================
    def getNombre(mi) -> str:
        return mi._nombre

    def getApellido(mi) -> str:
        return mi._apellido

    def getEdad(mi) -> int:
        return mi._edad 
