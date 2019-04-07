n = 6
a = 2

vec = [0]*n

less_sig_bit = n-1
vec[n-a:n] = [1]*a
print(vec)
while less_sig_bit > a - 1:
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
    
        print(vec)


    

