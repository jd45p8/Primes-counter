from count_primes import count_primes_up_to
from find_primes import find_primes

#n = int(input('Digite el n: '))
for i in range(1,100):
    print("n = " + str(i))
    print("  " + str(count_primes_up_to(i)) +  " - " +  str(len(find_primes(i))))
    if count_primes_up_to(i) != len(find_primes(i)):
        break
