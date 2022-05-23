# PROBLEM 10
from math import sqrt

def primo(n):
    if n % 2  == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

suma = 2
for n in range(3, 2000000, 2):
    if primo(n):
        suma += n
        
print(suma)

# OTRAS OPCIONES

# https://projecteuler.net/overview=010
# The sieve of Erathostenes








