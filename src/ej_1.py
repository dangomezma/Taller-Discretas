alphabet = "abcdefghijklmnopqrstuvwxyz"


# codificador cesar
def cesar_code(x:str, k:int):
    x = x.lower()
    result = ""
    # se crea una nueva cadena con los k desplazamientos de cada caracter
    for i in x:
        if i in alphabet:
            position = alphabet.index(i)
            # se reinicia el indice al llegar al final del abecedario
            if (position + k) < 26:
                result += alphabet[position + k]
            else:
                result += alphabet[(position + k)-26]
        else:
            result += i
    return result

# decodificador cesar
def cesar_decode(x:str, k:int):
    # en vez de ir correr el indice k veces, resta el indice k veces 
    result = cesar_code(x, -k)
    return result

# retorna todas las posibles codificaciones del string
def bruteforce(x:str):
    for i in range(26):
        result = cesar_decode(x, i)
        print(f"{i}: {result}")

