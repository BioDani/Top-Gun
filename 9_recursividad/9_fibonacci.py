serie = list()
def fibonacci( n = int):
    if n == 1 or n == 2: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(1, 10)])
print("lizz"[0:2])