def main():
    counts = dict()
    try:
        with open('../data/fragmento_libro.txt','r') as file:
            for line in file:
                line = line.replace(',','')
                line = line.replace('.','')
                line = line.replace(';','')
                line = line.replace('—','')
                
                line = line.lower()
                lst = line.split(' ')
                
                for word in lst:
                    counts[word] = counts.get(word, 0) + 1
        print(counts)
        
    except FileNotFoundError as error:
        print(error)
    else:
        print('Completed!')

    
if __name__ == '__main__':
    main()