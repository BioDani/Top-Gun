import time
import random 

def time_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time() 
        total_time = end_time - start_time
        print(f'Total time (s):{total_time}')
    return wrapper

def generate_list( start: int, end: int, n_elements: int):
    return [random.randint(start, end) for i in range(0, n_elements)]

@time_decorator
def sort_list( lst: list):
    lst.sort()
    print(lst)

def main():
    lst = generate_list(start=1,end=10,n_elements=10)
    sort_list(lst)
    
if __name__ == '__main__':
    main()