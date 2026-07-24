import numpy as np

"""
holas, para este ejercicio solo tienes que llamar a quibits(), solo es una simulacion

"""
def qubits():
    
    estado = np.array([1, 0]) # esto representa el qubit en estado |0⟩ con 100% certeza    
    # estado[0] es alpha (asociado a 0)
    # estado[1] es beta  (asociado a 1)

    X = np.array([[0,1],
                  [1,0]])

    Z = np.array([[1,0], 
                  [0,-1]])

    H = (1/(np.sqrt(2)))*np.array([[1,1], 
                               [1,-1]])


    # se crean nuevos estados multiplicando las matrices (compuertas) por el vector estado
    estado_x = X @ estado
    estado_z = Z @ estado
    estado_h = H @ estado

    # el * sirve para desempaquetar la tupla que viene de prob
    x_0, x_1= simulacion(*prob(estado_x))
    z_0, z_1 = simulacion(*prob(estado_z))
    h_0, h_1 = simulacion(*prob(estado_h))

    print("Para la compuerta X la frecuencia es:")
    print(f"0: {x_0} veces ({x_0/1000*100}%)")
    print(f"1: {x_1} veces ({x_1/1000*100}%)")

    print("Para la compuerta Z la frecuencia es:")
    print(f"0: {z_0} veces ({z_0/1000*100}%)")
    print(f"1: {z_1} veces ({z_1/1000*100}%)")

    print("Para la compuerta H la frecuencia es:")
    print(f"0: {h_0} veces ({h_0/1000*100}%)")
    print(f"1: {h_1} veces ({h_1/1000*100}%)")


    print("=== Casos especificos ===\n")

    # Caso 1: X|0> = |1>
    print("Caso 1: X|0> = |1>")
    print("La compuerta X actua como un NOT: invierte el estado")
    print(f"Estado obtenido tras aplicar X: {estado_x}")
    if np.array_equal(estado_x, np.array([0, 1])):
        print("Correcto: el qubit paso de |0> a |1> exactamente\n")
    else:
        print("Error: el resultado no coincide con |1>\n")

    # Caso 2: H|0> produce ~50%/50%
    print("Caso 2: H|0> produce probabilidades cercanas a 50%/50%")
    p0_h, p1_h = prob(estado_h)
    print(f"Probabilidad de medir 0: {p0_h:.4f}")
    print(f"Probabilidad de medir 1: {p1_h:.4f}")
    # se usa .allclose para verificar que sean muy similares (la tolerancia es estricta) y se usa en vez de .equal para evitar problemas de errores numericos pequeños
    if np.allclose([p0_h, p1_h], [0.5, 0.5]):
        print("Correcto: la compuerta H puso al qubit en una superposicion equilibrada,")
        print("es decir, no favorece ni al 0 ni al 1 al medirlo\n")
    else:
        print("Error: las probabilidades no estan cerca de 50%/50%\n")

    # Caso 3: HH|0> = |0>
    print("Caso 3: HH|0> = |0>")
    estado_h2 = H @ estado_h
    print(f"Estado obtenido tras aplicar H dos veces: {estado_h2}")
    if np.allclose(estado_h2, np.array([1, 0])):
        print("Correcto: aplicar H dos veces seguidas regresa el qubit a su estado original")
        print("El pequeño valor distinto de cero que se ve arriba (ej. 1e-17) no es un error")
        print("de logica, sino imprecision numerica normal al trabajar con raices cuadradas")
        print("en punto flotante. Por eso se compara con una tolerancia (np.allclose) en vez")
        print("de una igualdad exacta.\n")
    else:
        print("Error: aplicar H dos veces no devolvio el estado original.\n")

def prob(estado):

    prob_0 = estado[0] ** 2
    prob_1 = estado[1] ** 2
    return prob_0, prob_1

def simulacion(pr_0, pr_1):
    # random choise como su nombre lo dice escoje entre 0 y 1 aleatoriamente 1000 veces en este caso y regresa un array de 1000 numeros distribuidos segun la probabilidad
    resultado = np.random.choice([0,1], size=1000, p=[pr_0, pr_1])
    ceros  = np.sum(resultado == 0)
    unos  = np.sum(resultado == 1)
    return ceros, unos




qubits()