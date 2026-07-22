import random

M = int(1000003)


def MPC (x:list):
    # se inicializan los 3 servidores
    server1 = []
    server2 = []
    server3= []
    # para cada nota se definen las 3 variables y se manda cada una a su servidor correspondido
    for i in x:
        s1 = random.randrange(0, M)
        s2 = random.randrange(0, M)
        s3 = (i - s1 - s2) % M
        server1.append(s1)
        server2.append(s2)
        server3.append(s3)
    # se suman todas las variables de cada servidor, se suman sus resultados y se aplica modulo M lo que nos da el total de la suma de las notas
    total = ((sum(server1) % M) + 
             (sum(server2) % M) + 
             (sum(server3) % M)) % M
    average = total/len(x)
    return total, average

"""
hola alek como estas que tal tu dia, medio dia o noche? 
necesito q para este hagas una verificacion para el input x q es una lista
la lista tienen q ser enteros del 0 al 50 :)
thx

"""