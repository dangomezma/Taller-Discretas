import math

def Frecuency(x:str):
    used = []
    answer = []
    for i in x:
        if i not in used:
            answer.append(x.count(i))
            used.append(i)
    return answer

def Probability(x:str):
    frecuencies = Frecuency(x)
    answer = []

    for i in frecuencies:
        answer.append((i / len(x)))

    return answer

def Entropy(x:str):
    entropy = 0
    probabilities = Probability(x)

    for p in probabilities:
        entropy += p * math.log2(p)

    return -entropy


def Shannon(x:str):
    x = x.lower()
    no_repetitions = ""

    for i in x:
        if i not in no_repetitions:
            no_repetitions += i

    # Frecuency
    print("Frecuencia de cada simbolo")
    for i in range(len(no_repetitions)):
        print(f"{no_repetitions[i]}: {Frecuency(x)[i]}")
    
    # Probability
    print("Probabilidad de cada simbolo")
    for i in range(len(no_repetitions)):
        print(f"{no_repetitions[i]}: {Probability(x)[i]:.2f}")

    #Entropy
    print("Entropia")
    print(f"{Entropy(x)} bit/simbolo")

def Compare(x:str, y:str):
    H1 = Entropy(x.lower())
    H2 = Entropy(y.lower())

    print(f"Entropía texto 1: {H1:.4f} bits/símbolo")
    print(f"Entropía texto 2: {H2:.4f} bits/símbolo")

    if H1 > H2:
        print("El texto 1 tiene mayor entropía.")
        print("Esto significa que tiene mayor incertidumbre y variedad de simbolos")
    elif H2 > H1:
        print("El texto 2 tiene mayor entropia")
        print("Esto significa que tiene mayor incertidumbre y variedad de simbolos")
    else:
        print("Ambos textos tienen la misma entropia")

def HuffmanFrequencies(x:str):
    frequencies = {}

    for i in x:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    return frequencies


def BuildHuffmanTree(frequencies):
    nodes = []

    # Crear nodos como [simbolo, frecuencia]
    for symbol, frequency in frequencies.items():
        nodes.append([symbol, frequency])

    while len(nodes) > 1:
        # ordenar de menor a mayor frecuencia
        nodes.sort(key=lambda x: x[1])

        left = nodes.pop(0)
        right = nodes.pop(0)

        # unir los dos nodos menos frecuentes
        new_node = [
            [left, right],
            left[1] + right[1]
        ]

        nodes.append(new_node)

    return nodes[0]


def GenerateCodes(tree, code="", codes={}):
    # Si es un simbolo, guardar su codigo
    if isinstance(tree[0], str):
        codes[tree[0]] = code
        return codes

    # recorrer izquierda y derecha
    GenerateCodes(tree[0][0], code + "0", codes)
    GenerateCodes(tree[0][1], code + "1", codes)

    return codes


def HuffmanCodes(x:str):
    frequencies = HuffmanFrequencies(x)

    tree = BuildHuffmanTree(frequencies)

    codes = GenerateCodes(tree)

    return codes


def HuffmanAverage(x:str):
    codes = HuffmanCodes(x)

    average = 0

    for symbol in codes:
        probability = x.count(symbol) / len(x)
        bits = len(codes[symbol])

        average += probability * bits

    return average


"""
aqui toca hacer una comparacion entre huffman y la entropia 
algo como 

print(HuffmanCodes(texto))

longitud promedio de huffman:
entropia shannon:
"""