#(A AND B) OR (NOT C)
def expr1(A, B, C):
    return (A and B) or (not C)
#(A XOR B) AND C
def expr2(A, B, C):
    return (A ^ B) and C
#(A OR B) AND (NOT A OR C)
def expr3(A, B, C):
    return (A or B) and ((not A) or C)
#(A AND B) OR (C AND (NOT D))
def expr4(A, B, C, D): 
    return (A and B) or (C and (not D))
#(A XOR B) AND (C OR D)
def expr5(A, B, C, D):
    return (A ^ B) and (C or D)
#((NOT A) OR B) AND (C XOR D)
def expr6(A, B, C, D):
    return ((not A) or B) and (C ^ D)

"""
holas 
en este la idea es que puedan elegir mostrar la tabla de verdad de las expresiones de arriba (funciones que hare debajo de esto)
o que puedan ingresar su propia expresion logica (me voy a matar)
para la primera opcion necesito q aqui pongas algo como 
de cual de las siguientes expresiones deseas la tabla de verdad
1 (A AND B) OR (NOT C)
2 (A XOR B) AND C
3 (A OR B) AND (NOT A OR C)
4 (A AND B) OR (C AND (NOT D))
5 (A XOR B) AND (C OR D)
6((NOT A) OR B) AND (C XOR D)

para que te sea mas facil pensaba hacer una funcion abajo que mande la tabla seleccionada con un input del 1 al 6
y que eso retorne un print con la tabla, pero pues si te sientes comodo de hacerlo de otra forma adelante

"""

def tables(x:int):
    if x in [1, 2, 3]:
        print("+-------+-------+-------+-----------+")
        print("|   A   |   B   |   C   | Resultado |")
        print("+-------+-------+-------+-----------+")
    else:
        print("+-------+-------+-------+-------+-----------+")
        print("|   A   |   B   |   C   |   D   | Resultado |")
        print("+-------+-------+-------+-------+-----------+")
    if x == 1:
        for A in [False, True]:
            for B in [False, True]:
                for C in [False, True]:
                    print(f"| {A:^5} | {B:^5} | {C:^5} | {expr1(A,B,C):^9} |")
        print("+-------+-------+-------+-----------+")

    elif x == 2:
            for A in [False, True]:
                for B in [False, True]:
                    for C in [False, True]:
                        print(f"| {A:^5} | {B:^5} | {C:^5} | {expr2(A,B,C):^9} |")
    elif x == 3:
            for A in [False, True]:
                for B in [False, True]:
                    for C in [False, True]:
                        print(f"| {A:^5} | {B:^5} | {C:^5} | {expr3(A,B,C):^9} |")
            print("+-------+-------+-------+-----------+")

    elif x == 4:
            for A in [False, True]:
                for B in [False, True]:
                    for C in [False, True]:
                        for D in [False, True]:
                            print(f"| {A:^5} | {B:^5} | {C:^5} | {D:^5} | {expr4(A,B,C,D):^9} |")
            print("+-------+-------+-------+-------+-----------+")
    elif x == 5:
            for A in [False, True]:
                for B in [False, True]:
                    for C in [False, True]:
                        for D in [False, True]:
                            print(f"| {A:^5} | {B:^5} | {C:^5} | {D:^5} | {expr5(A,B,C,D):^9} |")
            print("+-------+-------+-------+-------+-----------+")

    else:
            for A in [False, True]:
                for B in [False, True]:
                    for C in [False, True]:
                        for D in [False, True]:
                            print(f"| {A:^5} | {B:^5} | {C:^5} | {D:^5} | {expr6(A,B,C,D):^9} |")
            print("+-------+-------+-------+-------+-----------+")


def concrete_expression(x:int, A:bool, B:bool, C:bool, D:bool=False):
    if x == 1:
            return expr1(A,B,C)
    elif x ==2:
            return expr2(A,B,C)
    elif x ==3:
            return (expr3(A,B,C))
    elif x ==4:
            return expr4(A,B,C,D)
    elif x ==5:
            return expr5(A,B,C,D)
    elif x ==6:
             return expr6(A,B,C,D)

