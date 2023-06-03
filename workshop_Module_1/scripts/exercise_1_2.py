def convert_F_to_C( f : float)  :
    
    """Convert from °F to °C.

    Convert between Fahrenheit and Celsius scales. 

    Args:
        f: Float number corresponding to a temperature in Fahrenheit scale. 

    Returns:
        float: temperature in Celsius scale. 
    """
    
    return (f - 32) * (5/9)


def main():
    try:
        f = float(input('Insert the temperature (°F):'))  
        assert isinstance(f, float)
        if f >= -459.67:
            c = "%.3f"%convert_F_to_C(f)
            print(f'{"%.2f"%f} °F is equal to {c} °C.')
        else:
            c = "%.2f"%convert_F_to_C(f)
            print(f'{"%.2f"%f} °F is equal to {c} °C; but {c} \
                in under the absolute zero -the lowest possible \
                temperature theoretically (-273.15 °C).')
            
    except Exception as error: 
        
        if isinstance(error, TypeError):
            print(error)
        print(error)
        
    else:
        print('Completed!')

if __name__ == '__main__':
    main()
