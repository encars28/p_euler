# PROBLEM 9
from math import sqrt

def perfect_square(n):
    sq = int(sqrt(n))

    return ((sq*sq) == n)


for a in range(1000):
    for b in range(a + 1, 1000):
        if perfect_square(a*a + b*b):
            c = int(sqrt(a*a + b*b))
            if a + b + c == 1000:
                print(a*b*c)

# OTRAS OPCIONES

# It can easily be seen that for every Pythagorean triplet a > 3 and a + b + c is
# even, you might want to prove that yourself.
# The most straightforward approach is to simply loop over a and b and then check
# whether a2 + b2 = (s − a − b)^2. From the condition a < b < c, we conclude that
# a <= (s − 3)/3 and b < (s − a)/2

# otro metodo que esta en el pdf y para el que hay q hacer mates chungas con el mcd/mcm

# https://projecteuler.net/overview=009




