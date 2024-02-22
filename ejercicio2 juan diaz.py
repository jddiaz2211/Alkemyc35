class Animal:
    def __init__(self, cantidad_patas):
        self.cantidad_patas = cantidad_patas
    
    def comer(self):
        return "Estoy comiendo, rico"

class Perro(Animal):
    def __init__(self, cantidad_patas, nombre, raza):
        super().__init__(cantidad_patas)
        self.nombre = nombre
        self.raza = raza
    
    def correr(self):
        return "Estoy corriendo"

class Aguila(Animal):
    def volar(self):
        return "Estoy volando"


perro = Perro(4, "doki", "Corgi")
print(perro.comer())
print (f"""{perro.nombre} ya comio""")
print (".........")
print(perro.correr())
print (f"""{perro.nombre} estaba corriendo""")
print (".........")


aguila = Aguila(2)
print(aguila.comer())
print (".........")
print(aguila.volar())
