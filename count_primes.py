from count_multiples import count_multiples_up_to as cm_up_to
from count_multiples import count_common_multiples_up_to as ccm_up_to
from find_primes import find_primes as fp

from math import sqrt,ceil,log10

# Cuenta los primos que hay desde 1 hasta n
def count_primes_up_to(n):
    # Se descarta el 1 como primo
    primes = n - 1
    
    # Primos menores o iguales a la raíz de n para verificar la primalidad de los número desde 1 hasta n
    v_primes = fp(ceil(log10(sqrt(n))))

    # Se descartan como primos todos los múltiplos de los primos menores o iguales que la raiz del n
    for v_prime in v_primes:
        not_primes = cm_up_to(v_prime,n) - 1
        # Se quitan los múltiplos comunes entre 2 primos para evitar la sobre eliminación de no primos
        i = 0
        while v_primes[i] < v_prime:
            not_primes -= ccm_up_to(v_prime,v_primes[i],n)
            i += 1
        
        primes -= not_primes

    return primes