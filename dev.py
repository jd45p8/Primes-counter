from time import time
from count_primes import count_primes_up_to

n = int(input('Digite el n: '))
t = time()
primes = count_primes_up_to(n)
t = time() - t

print(primes)
print("Tiempo: " + str(t))