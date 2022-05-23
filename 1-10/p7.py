# PROBLEM 7
from math import sqrt

def primo(n):
    if n % 2  == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

primes = [2, 3, 5, 7, 11, 13, 17, 19]
n = 23

while len(primes) < 10001:
    if primo(n):
        primes.append(n)

    n += 2

print(primes[-1])

# https://projecteuler.net/overview=007

