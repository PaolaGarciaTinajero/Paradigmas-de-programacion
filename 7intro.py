#==================================
# PROGRAMACIÓN ORIENTADA A OBJETOS 
#==================================

#==================================
# Una clase para un objeto vacío 
# No está tan vacío, necesita
# la palabra pass = pasar 
#==================================
class ObjetoVacio:
    pass

#===========================
# Nada es un ObjetoVacio
#===========================
nada = ObjetoVacio()
print(type(nada))

#======================
# La clase llanta 
#======================
class Llanta:
    #=====================================
    # Variable cuenta es de toda la clase
    #=====================================
    cuenta = 0
    #=====================================
    # Función constructora de identidad 
    # _init_ es una función reservada
    # comienza con uno mismo: self 
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #=====================================
    def _init_(mi, radio = 50, ancho = 30, presión = 1.5):
        # variable de la estructura completa Llanta 
        Llanta.cuenta += 1
        # variable exclusivas de cada objeto 
        mi.radio = radio 
        mi.ancho = ancho
        mi.presión = presión 

#==============================
# Objetos (instanciados)
#==============================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#==================================
# Objeto que contiene otros objetos
#==================================
class Coche:
    def _init_(mi, ll1, ll2, ll3, ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta) # Variable global de la clase 
print("Presión de la llanta 4 = ", llanta4.presión) # Presión de la llanta 4 
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta1.presión)

#==================
# Encapsulamiento
#==================


#=============================================================
# Uso de la función de python property para poner y obtener atributos
#=============================================================
class Estudiante:
    def _init_(mi):
        mi._nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamó a ponerme_nombre')
        mi._nombre = nombre 
    def obtener_nombre(mi):
        print('se llamó a obtener_nombre')
        return mi._nombre
    nombre = property(obtener_nombre, ponerme_nombre)

#==========================================
# Crear objeto estduainre sin nombre 
#==========================================
estudiante = Estudiante()

#===============================================================# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre 
# (sin tener que llamar explícitamente la función)
#===============================================================
estudiante.nombre = "Diego"

#==============================================================
# Obtener el nombre con el método obtener_nombre 
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que llamar explicitamente a la función obtener_nombre 
#===============================================================
print(estudiante.nombre)

# Esto no funciona
# print(estudiante._nombre)

#=================================
# Herencia de clases
#=================================
class Cuadrilatero:
    def _init_(mi, a, b, c, d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d

    def perimetro(mi):
        p = mi.lado1 + milado2 + mi.lado3 + mi.lado4
        print("perimetro = ", p)
        return p

#=====================================
# Su hijo rectángulo 
# Rectángulo es hijo de Cuadrilatero
# Rectángulo(Cuadrilatero)
#=====================================
class Rectangulo(Cuadrilatero):
    def _init_(self, a , b):
        #=============================
        # Constructor de su madre
        #=============================
        super()._init(a, b, a, b)

#===========================
# Su hijo cuadrado
# Hijo de Rectángulo
#===========================
class Cuadrado(Rectangulo):
    def _init_(self, a):
        super()._init(a, a)

    def area(self):
        area = self.lado1**2
        return area
    
    # def perimetro(self):
    #     p = 4.0*self.lado1
    #     print("perimetro = ", p)
    #     return p 

#============================
# Crear un cuadrado 
#============================
cuadrado = Cuadrado(5)

#==============================================================
# Llamar al método perímetrp de su abuelo Cuadrilatero
#==============================================================
perimetro1 = cuadrado1.perimetro()

#==================================
# Llamar a su propio método área
#==================================
area1 = cuadrado1.area()

print("Perímetro = ", perimetro1)
print("Área = ", area1)

#==============================================================
# Sobre-escribir un método de su madre o abuela o tatarabuela
# Es volver a definir una función la existente
#==============================================================

