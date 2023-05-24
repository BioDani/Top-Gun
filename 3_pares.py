def esPar( numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
    lista = input('Ingrese lista')
    pares = [ x for i in lista if esPar(i)]
    impares = [ x for i in lista if not esPar(i)]

    diccionario = {
        "Promedio" : sum(lista)/len(lista),
        "Pares"  : pares,
        "impares" : impares
    }

    print(diccionario)