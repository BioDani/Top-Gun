# sumar( n ) = 1 + 2 + ... + (n-1) + n 

def sumar(n):
    if n == 0: 
        return n
    else:
        return n + sumar(n - 1)
    
print(sumar(4))