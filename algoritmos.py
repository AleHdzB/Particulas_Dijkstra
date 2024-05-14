import math
from heapq import heappush, heappop

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    return round (distancia,2)

def get_puntos(particulas):
    puntos=[]
    for particula in particulas:
        r = particula.red
        g = particula.green
        b = particula.blue

        x_origen = particula.origen_x
        y_origen = particula.origen_y

        x_destino = particula.destino_x
        y_destino = particula.destino_y
        puntos.append([x_origen, y_origen, r, g, b])
        puntos.append([x_destino, y_destino, r, g, b])

    return puntos

def fuerza_bruta(puntos_list):
    resultado = []
    for punto_i in puntos_list:
        x1, y1, _, _, _ = punto_i  # Solo necesitamos las coordenadas x e y de punto_i
        min_distancia = 10000
        punto_cercano = (0, 0)
        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2, y2, _, _, _ = punto_j  # Solo necesitamos las coordenadas x e y de punto_j
                distancia = distancia_euclidiana(x1, y1, x2, y2)
                if distancia < min_distancia:
                    min_distancia = distancia
                    punto_cercano = (x2, y2)
        resultado.append((punto_i, punto_cercano))
    return resultado

def dijkstra(grafo, inicio):
    distancia = {nodo: float('inf') for nodo in grafo.obtener_vertices()}
    predecesor = {nodo: None for nodo in grafo.obtener_vertices()}
    distancia[inicio] = 0
    cola_visitados = [(0, inicio)]
    while cola_visitados:
        distancia_actual, nodo_actual = heappop(cola_visitados)
        if distancia_actual > distancia[nodo_actual]:
            continue
        for vecino, peso in grafo.obtener_aristas(nodo_actual):
            distancia_nueva = distancia_actual + peso
            distancia_nueva = round(distancia_nueva,2)
            if distancia_nueva < distancia[vecino]:
                distancia[vecino] = distancia_nueva
                predecesor[vecino] = nodo_actual
                heappush(cola_visitados, (distancia_nueva, vecino))
    return distancia, predecesor

