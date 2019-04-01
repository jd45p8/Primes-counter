# Cuenta los múltiplos de a desde 1 hasta n
def count_multiples_up_to(a,n):
    return int((n-(n%a))/a)

# Cuenta los mútiplos comunes de a y b hasta n
def count_common_multiples_up_to(a,b,n):
    if a != b:
        return count_multiples_up_to(a*b,n)
    else:
        return count_multiples_up_to(a,n)
