def main():
    try:
        number_1 = float(input('Insert a number: '))
        number_2 = float(input('Insert a number: '))

        assert isinstance(number_1, float)
        assert isinstance(number_2, float)
        
        print(f'The suma is equal to {number_1 + number_2}')
    
    except (KeyboardInterrupt, Exception) as error: 
        print(error)
    else:
        print('Completed!')
    
if __name__ == '__main__':
    main()
    