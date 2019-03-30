import numpy as np

vec = np.zeros((1000,1))
i = 2
while i <= 100:
    j = i
    while j <= 1000:
        vec[j-1,0] = j
        j += i
    if i > 2:
        i += 1
    else:
        i += 1

print(vec)