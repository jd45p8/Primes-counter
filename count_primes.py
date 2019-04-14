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
    v_primes_count = len(v_primes)

    # Se descartan como primos todos los múltiplos de los primos menores o iguales que la raiz del n
    not_primes = 0
    i = 0
    product = 1
    while product < n and i < v_primes_count:
        vec = []
        for j in range(0,i+1):
            vec.append(j-1)
        
        while product < n and vec[i] < v_primes_count - 1:
            product = 1
            for j in range(0,i+1):
                vec[j] += 1
                product *= v_primes[vec[j]]
                
                if (i+1)%2 is not 0:
                    not_primes += cm_up_to(product,n)
                    if (i+1) is 1:
                        not_primes -= 1
                else:
                    not_primes -= cm_up_to(product,n)
        
        i = i+1
        
    primes -= not_primes

    return primes
