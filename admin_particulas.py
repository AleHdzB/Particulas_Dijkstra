from particula import Particula
import json

class Admin:
    def __init__(self):
        self.__particulas = []
    def ordenar_particulas_por_id(self):
        self.__particulas.sort(key=lambda p: p.id)

    def ordenar_particulas_por_velocidad(self):
        self.__particulas.sort(key=lambda p: p.velocidad)

    def ordenar_particulas_por_distancia(self):
        self.__particulas.sort(key=lambda p: p.distancia,reverse=True)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0,particula)
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def mostrar(self):
        for p in self.__particulas:
            print(p)
    
    def __str__(self):
        return " ".join(
            str(p) + "\n" for p in self.__particulas
        )
    
    def __len__(self): #Sobrecarga de funcion len
        return(
            len(self.__particulas)
        )
    
    def __iter__(self): #Sobrecarga para poder hacer un objeto iterable
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
        
    def guardar(self, ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                #archivo.write(str(self))
                lista = [particula.to_dict() for particula in self.__particulas]
                print (lista)
                json.dump(lista,archivo,indent=5)
                return 1
        except:
            return 0
        
    def abrir(self, ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                #archivo.write(str(self))
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
        except FileNotFoundError:
            return 0
"""
admin = Admin()

p01 = Particula(1,1,1,1,1,1,1,1,1)
p02 = Particula(2,2,2,2,2,2,2,2,2)

admin.agregar_final(p01)
admin.agregar_inicio(p02)

admin.mostrar()
"""
