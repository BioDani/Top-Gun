def factorial(n = int):
    if n == 1:
        #Plantear el caso base que es el factorial(1)
        # Sino, da error porque supera el stack de python.
        return 1
    else:
        return n * factorial(n-1)

print(factorial( 3))