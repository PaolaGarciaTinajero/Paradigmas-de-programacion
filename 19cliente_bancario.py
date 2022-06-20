#==========================
# Clase ClienteBancario
#==========================
class ClienteBancario:
    _nombres: str = None
    _apellido: str = None
    _edad: int = 0
    _balanceDeCUenta: float = 0.0

    def _init_(self, nombres:str, apellidos:str, edad:str = 0, balanceDeCuenta:float =  0.0):
        self._validarEdad(edad)
        self._validarCantidad(balanceDeCuenta)
        self.nombres = nombres 
        self.apellidos = apellidos
        self._edad = edad
        selfbalanceDeCuentas = balanceDeCuentas 

    def getNombreCompleto(self) -> str:
        return self.Nombres + " " + self.apellidos

    def _mandarEmail(self, titulo:str, texto:str) -> None:
        print("mandar email: " + titulo + " con texto: " + texto)
    def _enviarBalanceAlBanco(self, cantidad:float) -> None:
        print("Enviando cantidad: " + str(cantidad) + " al banco...")

#====================================================
# Método privado con dos guiones bajos
# Si la edad es menor que 18 genera un error
#====================================================
def _validerEdad(self, edad:int) -> None:
    if edad < 18:
        raise Exception("Es menor de edad")

    def imprimirInfo(self) -> str:
        return "Nombre: " + self.getNombreCompleto() + ", Edad: " + str(self._edad) + ", Balance: " + str(self._balanceDeCuenta)

#=========================================================
# Método provado que checa si el balance es negativo
# y genera un error
#=========================================================
def _validarCantidad(self, balanceDeCuenta:float) -> None:
    if balanceDeCuenta < 0: 
        raise Exception("El balance en la cuenta no puede ser negativo")

def guardarDinero(self, cantidad:float) -> None:
    self._balanceDeCuenta = self._balanceDeCuenta + cantidad
    self._mandarEmail("---- guardando depósito ----", " se recibieron " + str(cantidad))

def retirarDinero(self, cantidad:float) -> None:
    cantidadFinal = self._balanceDeCuenta - cantidad
    self._validarCantidad(cantidadFInal)
    self._balanceDeCuenta = cantidadFinal 
    self.mandarEmail("---- retirando dinero ----", " se retiró " + str(cantidad))
    self._enviarBalanceAlBanco(cantidad))

