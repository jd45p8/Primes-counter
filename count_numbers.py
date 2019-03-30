import array
import numpy as np


n = 1000
vec = array.array('b',[0b0]*n)
vec[0] = 0b1
i = 2
for i in [2,3,5,7]:
    j = i*2
    while j <= n:
        vec[j-1] = 0b1
        j += i
    if i > 2:
        i += 2
    else:
        i += 1

cont = 0
for i in range(0,n,1):
    if(vec[i] == 1):
        cont += 1
    else:
        print(i+1)
print(n-cont)