from count_multiples import count_multiples_up_to as cm_up_to
from count_multiples import count_common_multiples_up_to as ccm_up_to
from math import sqrt,ceil

# Cuenta los primos que hay desde 1 hasta n
def count_primes_up_to(n):
    # Se descarta el 1 como primo
    primes = n - 1

    # Se descartan todos los pares como posibles primes a excepción del 2
    primes = primes - cm_up_to(2,n) + 1
    
    i = 3
    limit = ceil(sqrt(n))


    while i <= limit:
        # Se descartan todos los números que puedan ser generados como múltiplo de otro, excepto el mismo porque 
        # si no es primo ya debe hacer sido eliminado por ser múltiplo de algún i anterior
        not_primes = cm_up_to(i,n) - 1

        # Se descartan para eliminar los múltiplos comunes entre 2 e i porque los de 2 ya fueron eliminados
        #not_primes -= ccm_up_to(i,2,n)

        # Se descartan como primos todos los múltiplos comunes entre los primeros 4 primos y el número actual
        for j in [2,3,5,7]:
            not_primes -= ccm_up_to(i,j,n)
            j += 2          

        primes -= not_primes
        i += 2
    return primes