# https://docs.python.org/3/library/exceptions.html


def main():
    try:
        a = float(input("Insert a number:"))
        b = float(input("Insert a number:"))
        
        # assert falla si lo que hay adelante es `false`
        assert isinstance(a, float)
        assert isinstance(b, float) 
        
        div = a/b 
        print(f'The division is equal to {"%.3f"%div}')
    except Exception as error:
        print(error)
    except KeyboardInterrupt as error:
        print(error)
    except AssertionError as error:
        print(error)  
    else:
        print('COMPLETED')
        pass
if __name__ == '__main__':
    main()