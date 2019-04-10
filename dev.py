from binary_vectors import next_binary_vector

n = 4
a = 2
vec = []
less_sig_bit = n-1
first = True
last = False

while last == False:
    vec,less_sig_bit,last = next_binary_vector(n,a,vec,less_sig_bit,first)
    if first:
        first = False
    print(vec)