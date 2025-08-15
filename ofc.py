x = 5

def fibonacci(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)
    
for x in range(1, x + 1):
    print(fibonacci(x))