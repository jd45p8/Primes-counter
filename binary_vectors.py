# Determina el sigiente vector binario de tamaño n que resulta al mover hacia la
# el bit menos significativo del array vec de tamaño n y con a bits en 1
# first es verdadero si es la primera iteración, las es verdadero si es la última
def next_binary_vector(n,a,vec,less_sig_bit,first):
    last = False
    if(first):    
        vec = [0]*n
        vec[n-a:n] = [1]*a        
        if n == a:
            last = True
            return vec,less_sig_bit,last
        else:
            return vec,less_sig_bit,last   

    i = less_sig_bit - 1
    shipment = 1

    while vec[i] == 1 and i > 0:
        shipment += 1
        i -= 1

    if vec[i] == 0:
        vec[i] = 1

        if shipment > 1:
            vec[i+1:i+shipment+1] = [0]*shipment

            vec[n-shipment+1:n] = [1]*(shipment-1)

            less_sig_bit = n-1            
        else:
            vec[less_sig_bit] = 0
            less_sig_bit -= 1
    
        if less_sig_bit <= a - 1:
            last = True
            return vec,less_sig_bit,last
        else:
            return vec,less_sig_bit,last

def next_binary_vector_with_static_s(n,a,s,vec,less_sig_bit,first):
    if first:
        less_sig_bit -= 1
    else:
        del vec[s]        
    
    vec, less_sig_bit, last = next_binary_vector(n-1, a-1, vec, less_sig_bit, first)
    vec.insert(s,1)
    return vec,less_sig_bit,last


    

