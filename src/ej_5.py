from copy import deepcopy as dp # para copiar el grafo y poder modifiacarlo sin dañar el original y hacer la comparacion
from ej_4 import calcular_ruta_mas_corta 

def del_station(grafo:dict, x:list):
    a = dp(grafo)

    #elimina la key de la estacion
    for estacion in x:
        a.pop(estacion)

    # elimina las conexiones con la estacion a cerrrar
    for station, connection in a.items():
        for estacion in x:
            if estacion in connection:
                connection.pop(estacion)
    return a


def compare(grafo:dict, estaciones_cerrar:list, pares:list):
    grafo_despues = del_station(grafo, estaciones_cerrar)

    resultado_antes = []
    resultado_despues = []
    #recorre la lista de pares origen destino y calcula su ruta, luego las guarda en la lista designada
    for origen, destino in pares:
        distancia, ruta = calcular_ruta_mas_corta(grafo, origen, destino)
        resultado_antes.append((origen, destino, distancia, ruta))

    #recorre la lista de pares origen destino y calcula su ruta, luego las guarda en la lista designada (verifica si se elimino el origen o destino en la ruta)
    for origen, destino in pares:
        if origen in estaciones_cerrar or destino in estaciones_cerrar:
            distancia, ruta = float('inf'), []
        else:
            distancia, ruta = calcular_ruta_mas_corta(grafo_despues, origen, destino)
        resultado_despues.append((origen, destino, distancia, ruta))
    return resultado_antes, resultado_despues


def reportar_cambios(resultado_antes, resultado_despues):
    reporte = []
    
    for antes, despues in zip(resultado_antes, resultado_despues):
        origen, destino, dist_antes, ruta_antes = antes
        _, _, dist_despues, ruta_despues = despues
        
        if dist_antes == float('inf'):
            estado = "Ya estaba desconectado antes del cierre"
            diferencia = "N/A"
        elif dist_despues == float('inf'):
            estado = "Quedo desconectado"
            diferencia = "N/A"
        elif dist_despues > dist_antes:
            estado = "Aumento"
            diferencia = dist_despues - dist_antes
        elif dist_despues == dist_antes:
            estado = "Sin cambio"
            diferencia = 0
        else:
            estado = "Disminuyo"  # caso raro, pero puede pasar si la ruta antes pasaba por la estación cerrada y había otro camino más corto
            diferencia = dist_despues - dist_antes
        
        reporte.append((origen, destino, dist_antes, dist_despues, diferencia, estado))
    
    return reporte



"""
aqui hice un test del archivo para q entiendas como manejar los retornos en el main :)
"""

if __name__ == "__main__":
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

    estaciones_a_cerrar = ['Centro']

    pares_a_probar = [
        ('Portal', 'Estadio'),
        ('Universidad', 'Parque'),
        ('Calle26', 'Biblioteca'),
        ('Museo', 'Universidad'),
        ('Portal', 'Centro'),  # incluye la estación cerrada -> debe salir "desconectado"
    ]

    resultado_antes, resultado_despues = compare(grafo_prueba, estaciones_a_cerrar, pares_a_probar)
    reporte = reportar_cambios(resultado_antes, resultado_despues)

    for fila in reporte:
        print(fila)