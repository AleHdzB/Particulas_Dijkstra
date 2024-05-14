from algoritmos import distancia_euclidiana, get_puntos
from random import randint

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_vertices_de_particulas(self, particulas):
        for particula in particulas:
            self.agregar_vertice((particula.origen_x, particula.origen_y))
            self.agregar_vertice((particula.destino_x, particula.destino_y))
                
    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self, vertice):
        return self.vertices[vertice]

    def __str__(self):
        return str(self.vertices)
    
    def agregar_aristas_entre_particulas(self, particulas):
        puntos = get_puntos(particulas)
        n = len(puntos)

        for i in range(n):
            punto_origen = (puntos[i][0], puntos[i][1])
            for j in range(i+1, n):  # Iterar sobre los vértices restantes
                punto_destino = (puntos[j][0], puntos[j][1])
                peso = distancia_euclidiana(punto_origen[0], punto_origen[1], punto_destino[0], punto_destino[1])

                if punto_origen in self.vertices and punto_destino in self.vertices:
                    self.vertices[punto_origen].append((punto_destino, peso))
                    self.vertices[punto_destino].append((punto_origen, peso))

"""
    def agregar_aristas_entre_particulas(self, particulas):
        puntos = get_puntos(particulas)
        x = randint(0, len(puntos) - 1)
        y = randint(0, len(puntos) - 1)
        
        # Agregar aristas entre el origen y el destino de cada partícula
        for i in range(0, len(puntos), 2):
            punto_origen = (puntos[i][0], puntos[i][1])
            punto_destino = (puntos[i + 1][0], puntos[i + 1][1])
            peso = distancia_euclidiana(punto_origen[0], punto_origen[1], punto_destino[0], punto_destino[1])
            self.vertices[punto_origen].append((punto_destino, peso))
            self.vertices[punto_destino].append((punto_origen, peso))
        # Agregar aristas adicionales entre el destino de una partícula y el origen de la siguiente
        for i in range(0, len(puntos) - 1, 2):
            punto_destino = (puntos[i + 1][0], puntos[i + 1][1])
            siguiente_punto_origen = (puntos[(i + 2) % len(puntos)][0], puntos[(i + 2) % len(puntos)][1])
            
            peso = distancia_euclidiana(punto_destino[0], punto_destino[1], siguiente_punto_origen[0], siguiente_punto_origen[1])
            
            if punto_destino in self.vertices and siguiente_punto_origen in self.vertices:
                self.vertices[punto_destino].append((siguiente_punto_origen, peso))
                self.vertices[siguiente_punto_origen].append((punto_destino, peso))
"""