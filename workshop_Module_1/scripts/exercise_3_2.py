def reverse_string( word : str):
    
    """Calculate the area of a rectangle.

    Description 
    
    Args:
        word (string): string not null.

    Returns:
        float: the reverse of a string

    Raises:
        AssertionError: If either a list, dictionary is provided.
        IndexError: If string has a length zero. 
        
    """
    
    if not isinstance( word, str):
        raise AssertionError('Must provide a string.')
    if not word:
        raise IndexError('The string is empty.')
    return word[::-1]

def main():
    try:
        print(reverse_string('daniel'))
    except IndexError as error:
        print(error)
    except AssertionError as error:
        print(error)
    else:
        print('Completed!')
    
if __name__ == '__main__':
    main()