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

