def is_prime( n: int):
    
    """ Prime numbers

    Prime numbers are positive integers greater than 1 that are only divisible by 1 and themselves.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        string: 'not prime' if it is 1 or a negative number
                'not prime' if it is divisible by a number diferent to 1 and itself (module equals 0)
                'prime' if it is not 1 or if it is not divisible por any number 
    """
     
    if n <= 1:
        return "not prime"
    for i in range(2, n):
        if n % i == 0:
            return "not prime"
    return "prime"
    

def main():
    try:
        number = int(input('Enter a int number:'))
        print(f'{number} is {is_prime(number)}.')
    except ValueError as error:
        print('Expected an integer (int) but received a different data type.')
    else:
        print('Completed')
    
if __name__ == '__main__':
    main()