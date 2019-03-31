import scipy.sparse as sp
import numpy as np

from math import sqrt


def find_primes(potencia):
    n = pow(10,potencia)
    vec = sp.lil_matrix((n,1), dtype=np.int8)

    vec[0] = 1
    primes = [2]
    prime = 2
    limit = sqrt(n)

    while True:
        j = prime*2
        # Marca con 1 los múltiplos de cuálquier primo
        while j <= n:
            vec[j-1] = 1
            j += prime
        
        # Hallar el último primo verificado
        prime += 1
        while vec[prime - 1] != 0 and prime <= limit:
            prime += 1

        if prime > limit:
            break
        else:
            primes.append(prime)
    
    j = prime
    while j < n:
        j = j+1
        if vec[j-1] != 0:
            pass
        else:
            primes.append(j)
    return primes
    #print('There is: ' + str(n - vec.count_nonzero()))
    #print('Time: ' + str(t))
    