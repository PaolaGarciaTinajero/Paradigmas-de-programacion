#======================================
# La clase A tiene tres números reales
#======================================
class A:
    _a:float = 0.0
    _b:float = 0.0
    _c:float = 0.0

    def _init_(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        selfc = c

#=========================================
# La clase B tiene dos números reales 
#=========================================
class B: 
    _d:float = 0.0 
    _e:float = 0.0

    def _init(self, d:float, e:float):
        self.d = d
        self.e = e

    #==================================================
    # Método sumar todo (internos + externos)
    #==================================================
    def sumar_todo(self, aa:float, bb:float):
        x:float = self.d + self.e + aa + bb
        return x 

#================
# ASOCIACIÓN
#================
# Usando objetos independientes 
objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)
print(objeto.sumar_todo(objetoA.a, objetoB.b))

#===================================================
# El objeto C tiene dos reales y un objeto A 
# El objeto A se instancia dentro de C
#===================================================
class C:
    _d:float = 0.0 
    _e:float = 0.0
    _Aa:A = None 

    def _init_(self, d:float, e:float):
        self.d = d
        self.e = e
        # A está instanciado adentro
        self.Aa = A(1.0, 2.0, 3.0)

    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa + self.Aa.b
        return x 

#============================
# COMPOSICÓN 
# Contiene otro objeto dentro
#============================
objetoC = C(4.0, 5.0)
print(objetoC.sumar_todo())

#==========================================================
# Objeto D tiene dos reales y un objeto A
# definido por fuera
#==========================================================
class D:
    _d:float = 0.0
    _e:float = 0.0
    _Aa:A = None 

    def _init_(self, d:float, e:float, Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa
    
    def sumar_todo(self):
        x:float = self.d + self.e + self.Aa.a + self.Aa.b
        return x 

#============================================
# AGREGACIÓN 
# Construye el objeto agregado por fuera
#============================================
objetoD = D(4.0, 5.0, objetoA)
print(objetoD.sumar_todo())
