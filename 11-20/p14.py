# PROBLEM 14

maximo = 1

for n in range(13, 1000000):
    count = 0
    original = n
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        
        count += 1

    if count > maximo:
        maximo = count
        print(count, original)

# https://projecteuler.net/overview=014
