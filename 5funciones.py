#====================
# Primera función 
#====================
def saludo():
    #======================================
    # Documentación rápida de la función 7
    #======================================
    """Esta función saluda"""
    print('¡Hola!, ¿cómo estás?')

#=======================
# Llamado de la función 
#=======================
saludo()

#================================
# Se ejecuta pero no se asigna 
#================================
saludo = saludo()

#====================
# Esto no funciona 
#====================
#print(salida)

#=========================
# Mostrar documentación 
#=========================
#help(saludo)

#==========================
# Función con argumento 
#==========================
def salu2(nombre):
    """ESta función te saluda por tu nombre"""
    print("¡Que onda", nombre, "!")
salu2("Paola")
salu2("Luis")

#=========================================
# Ahorrar trabajo del intérprete 
# nombre:str la variable nombre es un str 
#=========================================
def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("¡Qué onda", nombre, "!")
saludos("Paola")
a = 123
print(type(a))
saludos(a)

#=================================
# Función con muchos argumentos 
#=================================
def saludos_multiples(nombre1, nombre2, nombre3):
    """ESta función saluda a 3 personas al mismo tiempo"""
    print("Hola ", nombre1, ",", nombre2, "y", nombre3)
saludos_multiples("Gerardo", "Emi","Rocko")

#==============================================
# Función con cualquier número de argumentos 
#==============================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0 
    #====================================
    # end = es para ponerlo de corrido
    #====================================
    print("Hola ", end = "")
    while len(nombres) > i:
        # último nombre 
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            # cualquier otro nombre 
            print(nombres[i], end = ", ")
        i += 1 

muchos_saludos("Luis", "Paola", "Adriana", "Gerardo", "Jerry", "Emi", "Rocko", "Mich", "Nala")

def greet(firstname, lastname):
    print('Hello', firstname, lastname)

#==============================================
# Llamar la función con argumentos en desorden 
#==============================================
greet(lastname = 'Turin', firstname = 'Alan') # Se pueden especificar las variables en desorden

#======================================
# Función con argumentos escondidos **
#======================================
def greet(**person):
    #====================================================
    # persona tiene características firstname y lastname 
    #====================================================
    print('Hello', person['firstname'], person['lastname'])

greet(firstname = 'Alan', lastname = 'Turin')
greet(lastname = 'Turin', firstname = 'Alan')
greet(firstname = 'Bill', lastname = 'Gates', age = 55) # Sepueden psar más parámetros de los necesarios 

#======================================
# Función con valores por defecto 
#======================================
def greet(name = 'Guest'):
    print('Hello', name)

greet() # utiliza el valor dado de antemano 
greet('Steve')

#===========================
# Función con resultado
#===========================
def suma(a , b):
    return a + b 

#=====================================
# Programación funcional 
# Se pueden funciones en funciones 
#=====================================
total = suma(5, suma(10, 20))
print(total)

#==================================================
# Cálculo lambda 
# nombre de la función = lambda variable : función 
#==================================================
x_al_cuadrado = lambda x : x * x 
al = x_al_cuadrado(5)
print(al)

#===========================
# Lambda de varias varibles 
#===========================
suma = lambda x1, x2, x3: x1 + x2 + x3
print(suma(99, 98, 97))

sumas = lambda *x: x[0] + x[1] + x[2] + x[3]

print(sumas(100, 200, 300, 400))

#=========================================
# Uso de una función anónima 
# El argumento va afuera entre paréntesis
#=========================================
print((lambda x: x * x)(6)) # Función anónima 

#==================================
# Función con varible global 
# EVITE EL EXCESO!!!
#==================================
name = 'Paola'
def greet():
    global name # Para utilizar una variable global (que viene de fuera del bloque)
    name = 'Luis'
    print('Hello', name)

greet()

