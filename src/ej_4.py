import heapq #heapq permite ubicar en la primera posición de la lista el elemento con menor valor

def calcular_ruta_mas_corta(grafo: dict, origen: str, destino: str):
    # Inicializamos las distancias a infinito para todos los nodos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    
    # Diccionario para recordar de dónde venimos y poder reconstruir la ruta
    nodos_padre = {nodo: None for nodo in grafo}
    
    # La cola de prioridad almacenará tuplas: (distancia_acumulada, nodo_actual)
    cola_prioridad = [(0, origen)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        #Si ya sacamos el destino de la cola podemos terminar la búsqueda
        if nodo_actual == destino:
            break
            
        # Si la distancia en la cola es mayor a la ya registrada es obsoleta
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        # Exploramos las conexiones del nodo actual
        for vecino, peso_calle in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso_calle
            
            # Si encontramos un atajo más barato hacia el vecino, actualizamos
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                nodos_padre[vecino] = nodo_actual
                # Agregamos esta nueva ruta corta a la cola
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                
    # Reconstrucción del camino
    ruta = []
    nodo_rastreo = destino
    
    # Si la distancia al destino sigue siendo infinita, no hay conexión posible
    if distancias[destino] == float('inf'):
        return float('inf'), []
        
    while nodo_rastreo is not None:
        ruta.append(nodo_rastreo)
        nodo_rastreo = nodos_padre[nodo_rastreo]
        
    #El rastreo se hizo desde el destino hacia el origen
    ruta.reverse()
    
    #Distancia total y ruta encontrada
    return distancias[destino], ruta

#nauJ, testea con: 
"""
grafo_prueba = {
    'Portal': {'Calle26': 10, 'Universidad': 15},
    'Calle26': {'Portal': 10, 'Museo': 12, 'Centro': 20},
    'Universidad': {'Portal': 15, 'Centro': 10, 'Biblioteca': 5},
    'Museo': {'Calle26': 12, 'Centro': 8, 'Estadio': 25},
    'Centro': {'Calle26': 20, 'Universidad': 10, 'Museo': 8, 'Biblioteca': 12, 'Parque': 15},
    'Biblioteca': {'Universidad': 5, 'Centro': 12, 'Parque': 10},
    'Parque': {'Centro': 15, 'Biblioteca': 10, 'Estadio': 20},
    'Estadio': {'Museo': 25, 'Parque': 20}
}
"""
"""
origen_test = 'Portal'
destino_test = 'Estadio'
distancia_total, ruta_final = calcular_ruta_mas_corta(grafo_prueba, origen_test, destino_test)
"""



"""
print("\n=== RESULTADOS DE DIJKSTRA ===")
print(f"Origen: {origen_test}")
print(f"Destino: {destino_test}")
print(f"Distancia/Costo total: {distancia_total}")
print(f"Ruta óptima: {' -> '.join(ruta_final)}")
print("==============================\n")
"""
