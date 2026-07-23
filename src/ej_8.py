from typing import List, Set, Tuple

def _difieren_en_un_solo_bit(term1: str, term2: str) -> bool:
    """
    Verifica si dos cadenas binarias difieren en exactamente una posición.
    Ejemplo: '001' y '011' -> True.
    """
    diferencias = sum(1 for b1, b2 in zip(term1, term2) if b1 != b2)
    return diferencias == 1


def _fusionar_terminos(term1: str, term2: str) -> str:
    """
    Combina dos términos binarios reemplazando el bit diferente por un guion '-'.
    Ejemplo: '001' y '011' -> '0-1'.
    """
    resultado = [b1 if b1 == b2 else '-' for b1, b2 in zip(term1, term2)]
    return "".join(resultado)


def _obtener_implicantes_primos(minterminos: List[int], num_vars: int) -> List[str]:
    """
    Quine-McCluskey para encontrar agrupaciones
    """
    # Convierte los enteros a formato binario asegurando la longitud correcta (ej. 1 -> '001')
    grupos = [format(m, f'0{num_vars}b') for m in minterminos]
    implicantes_primos: Set[str] = set()
    
    while True:
        nuevos_grupos: Set[str] = set()
        marcados: Set[str] = set()
        
        # Comparamos todos los pares posibles buscando simplificaciones
        for i in range(len(grupos)):
            for j in range(i + 1, len(grupos)):
                if _difieren_en_un_solo_bit(grupos[i], grupos[j]):
                    termino_fusionado = _fusionar_terminos(grupos[i], grupos[j])
                    nuevos_grupos.add(termino_fusionado)
                    marcados.add(grupos[i])
                    marcados.add(grupos[j])
                    
        # Los términos que no se combinaron con nadie ya son irreducibles (implicantes)
        for g in grupos:
            if g not in marcados:
                implicantes_primos.add(g)
                
        # Condición de parada: si no logramos agrupar nada más, terminamos
        if not nuevos_grupos:
            break
            
        grupos = list(nuevos_grupos)
        
    return list(implicantes_primos)


def _generar_suma_de_productos(implicantes: List[str], num_vars: int) -> str:
    """
    Traduce los implicantes binarios a una expresión en forma Suma de Productos (SOP).
    Un '1' es la variable normal, un '0' es la variable negada (A'), un '-' se ignora.
    """
    variables = ['A', 'B', 'C', 'D'][:num_vars]
    terminos_sop = []
    
    for imp in implicantes:
        termino_actual = ""
        for i, char in enumerate(imp):
            if char == '1':
                termino_actual += variables[i]
            elif char == '0':
                termino_actual += f"{variables[i]}'"
                
        # Si el término quedó vacío (ej. todos son guiones '---'), significa que siempre es verdadero
        if not termino_actual:
            termino_actual = "1"
            
        terminos_sop.append(termino_actual)
        
    return " + ".join(terminos_sop) if terminos_sop else "0"


def _validar_tablas_de_verdad(minterminos: List[int], implicantes: List[str], num_vars: int) -> bool:
    """
    Comprueba que la expresión original y la simplificada tienen la misma tabla de verdad.
    Itera sobre las 2^n combinaciones posibles.
    """
    total_combinaciones = 2 ** num_vars
    todas_las_entradas = [format(i, f'0{num_vars}b') for i in range(total_combinaciones)]
    
    for entrada_bin in todas_las_entradas:
        # En el circuito original, la salida es 1 si la entrada está en los mintérminos
        es_verdadero_original = int(entrada_bin, 2) in minterminos
        
        # En el simplificado, es 1 si la entrada encaja en al menos un implicante primo
        es_verdadero_simplificado = any(
            all(b_imp == '-' or b_imp == b_ent for b_imp, b_ent in zip(imp, entrada_bin))
            for imp in implicantes
        )
        
        # Si difieren en un solo escenario, los circuitos no son lógicamente equivalentes
        if es_verdadero_original != es_verdadero_simplificado:
            return False
            
    return True


def simplificar_circuito(minterminos: List[int], num_vars: int) -> Tuple[str, bool]:
    """
    Función pública principal.
    Recibe la lista de mintérminos y la cantidad de variables.
    Retorna la expresión simplificada y un booleano confirmando la validación.
    """
    if not minterminos:
        return "0", True
        
    implicantes = _obtener_implicantes_primos(minterminos, num_vars)
    
    # Ordenamos para asegurar que los grupos más reducidos aparezcan primero en la lectura
    implicantes.sort(key=lambda x: x.count('-'), reverse=True)
    
    expresion_final = _generar_suma_de_productos(implicantes, num_vars)
    es_equivalente = _validar_tablas_de_verdad(minterminos, implicantes, num_vars)
    
    return expresion_final, es_equivalente


# minterminos_prueba = [1, 3, 5, 7]
# cantidad_variables = 3
    
# expresion_obtenida, tablas_coinciden = simplificar_circuito(minterminos_prueba, cantidad_variables)

#  print(f"Expresión simplificada: {expresion_obtenida}")
#  print(f"Verificación de tabla:  {'CORRECTA (Coinciden)' if tablas_coinciden else 'INCORRECTA'}")
    
   