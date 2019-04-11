from count_multiples import count_multiples_up_to as cm_up_to
from count_multiples import count_common_multiples_up_to as ccm_up_to
from binary_vectors import next_binary_vector_with_static_s
from find_primes import find_primes as fp
from math import sqrt, ceil


# Cuenta los primos que hay desde 1 hasta n
def count_primes_up_to(n):
    # Se descarta el 1 como primo
    primes = n - 1
    
    # Primos menores o iguales a la raíz de n para verificar la primalidad de los número desde 1 hasta n
    v_primes = fp(ceil(sqrt(n)))

    # Se descartan como primos todos los múltiplos de los primos menores o iguales que la raiz del n
    for i in range(0, len(v_primes)):
        not_primes = cm_up_to(v_primes[i], n) - 1

        # Se quitan los múltiplos comunes entre 2 primos para evitar la sobre eliminación de no primos
        for j in range(0, i):
            not_primes -= ccm_up_to(v_primes[i], v_primes[j], n)

        for a in range(3,i+2):
            vec = []
            less_sig_bit = i
            first = True
            last = False

            while last is False:
                vec, less_sig_bit, last = next_binary_vector_with_static_s(i+1, a, i, vec, less_sig_bit, first)
                if first:
                    first = False

                product = 1
                k = 0
                while k <= i:
                    if vec[k] == 1:
                        product *= v_primes[k]
                    k += 1
                if product > 1:
                    not_primes += cm_up_to(product, n)
        
        primes -= not_primes

    return primes
