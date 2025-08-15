def find_factors(n):
    factors = [] # make them all show up in one output
    divisor = 2 # start at two

    while n > 1: # divide until n = 1
        while n % divisor == 0: # continue only if rest of division is 0
            factors.append(divisor) # add it to the list
            n = n // divisor # continue with new number -> or infinite loop
        divisor += 1 # try a diff divisor
    
    print(factors)

find_factors(60)