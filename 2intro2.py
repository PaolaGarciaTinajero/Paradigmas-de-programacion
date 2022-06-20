#======================================================
# Input permite obtener datos del usuario en prompter 
#======================================================
nombre = input("Dame tu nombre: ")
print("Hola, como estás", nombre)

#=========================================
# Los enteros son de presición ilimitada
#=========================================
y = 50000000000000000000000000000000
print(y)

#=============================================================
# Se pueden delimitar números con guión bajo pero no con coma
#=============================================================
y = 5_000_000
print(y)

#=====================================================
# La función int() cambia strings y floats a enteros 
#=====================================================
numero = int(input("Dame tu edad: "))
type(numero)

#======================================================
# La notación científica de flotantes utiliza e o E
#======================================================
# 1.2 * 10 ^ {-9}
#=================
y = 1.2E-09
print(y)

#=========================================================
# La función float() convierte strings y enteros a floats 
#=========================================================
y = float("14.3")
print(y)

#=====================================================
# Los complejos se escriben con la raíz de menos uno
# j siempre con un número como prefijo
# no acepta la j suelta
#=====================================================
z = 1+1j

# suma +
# resta - 
# multiplicación *
# división /
# módulo %
# exponente **
# // función piso 
# funciones para transformar números int() float() complex()
# operaciones abs() round() pow()

print(round(3.14159, 4))

#===========================
# Strings de varias lineas 
#===========================
parrafo = """Data objects of the above types
are stored in a computer's memory for processing."""
print(parrafo)

#===============================================
# La función len() obtiene el tamaño del string
#===============================================
n = len(parrafo)
print(n)

#=============================================================
# Las letras en un string ocupan lugares como en un arreglo
# (también de atras para adelante comenzando en -1 el último)
#=============================================================
palabra = "Hola"
print(palabra[0])
print(palabra[-4])
