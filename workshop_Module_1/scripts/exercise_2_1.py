def generate_fibonacci(n : float = 10):
    
    """The fibonacci serie.

    Generate the n-terms of the fibonacci serie.
    
    Args:
        n(int): The n-terms to generate. By default n equals 10.

    Returns:
        list: List with the n-termns of the fibonacci.
    
    """
    
    serie = [0,1]
    for i in range(0, n-2):
        serie.append( serie[-2] + serie[-1])
    return serie

def main():
    print(generate_fibonacci())

if __name__ == '__main__':
    main()