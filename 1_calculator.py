def calculator(a:int,b:int):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    
    if b != 0:
        division = a/b
    else:
        division = "Not possible!"
    
    return f'Suma:{suma}\nResta:{resta}\nMultiplicación:{multiplicacion}\nDivisión:{division}'


a = float(input("Define number 1: "))
b = float(input("Define number 2: "))

print(calculator(a,b))