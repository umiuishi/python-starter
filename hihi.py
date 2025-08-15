n = 7

default_1 = 0 # starting numbers
default_2 = 1

for number in range(n): # random variable in for
    print(default_1) # 0 1 1 2 3 5 8

    sum = default_1 + default_2 # sum = 0 + 1
    default_1 = default_2 # 0 = 1
    default_2 = sum # 1 = 1
