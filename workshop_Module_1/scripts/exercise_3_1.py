def find_maximum( lst: list):
    
    """Find max value of a list.
 
    Args:
        lst(list): The length of the rectangle.

    Returns:
        float: The max value inside a numeric list.
    
    Raises:
        TypeError: If a list is not provided.
        ValueError: If all elements of the list are not either float or int 
    """
    
    if not isinstance(lst, list):
        raise TypeError('Must provide a list.')
    if not all(isinstance(i, float or int) for i in lst):
        raise ValueError("Must list all numeric elements.")

    return max(lst)
 
def main():
    
    try:
        values = eval(input('Insert list of numbers:'))
        print(find_maximum(values)) 
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
    else:
        print('Completed!')
    
if __name__ == '__main__':
    main()