# PROBLEM 3
from math import sqrt

def primo(n):
    if n % 2  == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


number = 600851475143
for n in range(int(sqrt(number)) - 1, 1, -2):
    if number % n == 0 and primo(n):
        print(n)

# OTRAS OPCIONES

# tambien se podia hacer haciendo la division entre primos tradicional
# para descomponer, haciendo un while del que se sale cuando el ultimo factor es 1
# para optimizar esto bastaria acotar un limete hacia arriba, que seria la raiz

# https://projecteuler.net/overview=003