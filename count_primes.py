from count_multiples import count_multiples_up_to as cm_up_to
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
    too_big = False
    while  not too_big and i < v_primes_count:
        # Se genera el primer vector de tamaño i+1 para
        too_big = True
        vec = []
        prod = []
        for j in range(0,i+1):
            vec.append(j)
            if j > 0:
                prod.append(prod[j-1]*v_primes[vec[j]])
            else:
                prod.append(v_primes[vec[j]])

        if (i + 1) % 2 is not 0:
            not_primes += cm_up_to(prod[i], n)
            if (i + 1) is 1:
                not_primes -= 1
        else:
            not_primes -= cm_up_to(prod[i], n)


        while vec[0] < v_primes_count-i-1:
            j = i
            while j > 0 and vec[j] == v_primes_count - (i - j) - 1:
                j -= 1

            vec[j] += 1
            if j > 0:
                prod[j] = v_primes[vec[j]]*prod[j-1]
            else:
                prod[j] = v_primes[vec[j]]

            for k in range(1, i - j + 1):
                vec[j + k] = vec[j] + k
                prod[j + k] = prod[j + k - 1]*v_primes[vec[j + k]]
                
            if (i+1)%2 is not 0:
                not_primes += cm_up_to(prod[i],n)
                if (i+1) is 1:
                    not_primes -= 1
            else:
                not_primes -= cm_up_to(prod[i],n)

            if too_big:
                if prod[i] < n:
                    too_big = False
        
        i = i+1
        
    primes -= not_primes

    return primes
