from count_multiples import count_multiples_up_to as cm_up_to
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

        for a in range(2,i+2):
            vec = []
            less_sig_bit = i
            first = True
            last = False

            while last is False:
                vec, less_sig_bit, last = next_binary_vector_with_static_s(i+1, a, i, vec, less_sig_bit, first)
                if first:
                    first = False

                product = 1
                j = 0
                while j <= i:
                    if vec[j] == 1:
                        product *= v_primes[j]
                    j += 1
                if product > 1:

                    if a%2 == 0:
                        not_primes -= cm_up_to(product, n)
                    else:
                        not_primes += cm_up_to(product, n)

            # Si el ultimo producto es mayor que n significa que los próximos también lo serán
            if product > n:
                break
        
        primes -= not_primes

    return primes
