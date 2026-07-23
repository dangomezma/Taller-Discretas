def extended_eu(a: int, b: int):
    if a == 0:
        return b, 0, 1
    
    mcd, x1, y1 = extended_eu(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return mcd, x, y


def rsa(p: int, q: int, e: int):

    n=p*q
    phi_n=(p-1)*(q-1)
    
    mcd, x, y = extended_eu (e, phi_n)
    
    if mcd != 1:
        raise ValueError("Error: mcd(e, phi(n)) != 1. El exponente 'e' no es válido.")
    
    #x puede ser negativo; x % phi_n lo convierte en el representante positivo válido para d.
    d = x % phi_n
        
    return n, phi_n, d

def m_descifrado(c: int, d: int, n: int):
    m_d = pow(c, d, n)
    return m_d

def cifrado(m: int, e: int, n: int):
    c = pow(m, e, n)
    return c