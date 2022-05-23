# PROBLEM 12

# INTENTOS QUE ME DABAN TIMEOUT

# # n = 5742
# n = 1
# # count = 0

# # while count < 500:
# while n < 50:
#     # count = 0
#     n += 1
#     number = int((n*(n+1))/2)

#     factors = [x for x in range(1, number + 1) if number % x == 0]

#     # for x in range(1, number + 1):
#     #     if number % x == 0:
#     #         count += 1

#     print(factors)

# from math import sqrt, prod

# def append_factor(number, prime, f):
#     if number % prime == 0:
#         f.append(1)
#         number = number / prime
#         while number % prime == 0:
#             f[-1] += 1
#             number = number / prime


# triangle = 28
# i = 7
# factors = []

# while prod(factors) < 500:
#     factors = []
#     i += 1
#     triangle += i
#     maxfactor = int(sqrt(triangle))
#     append_factor(triangle, 2, factors)

#     for n in range(3, maxfactor, 2):
#         append_factor(n, triangle, factors)

# print(triangle)       

# cargar lista de primos
from math import sqrt

with open("primes.txt", "r") as f:
    primes = f.read().replace("\n", "")
    primes = primes.split("-")
    primes = [int(n) for n in primes]

n = 7
number = 28
count = 1
while count < 500:
    count = 1
    for p in primes:
        if p > number:
            break

        c = 0
        while number % p == 0:
            c += 1
            number = number / p

        count *= (c + 1)

            
    if count == 1:
        for x in range(primes[-1] + 2, int(sqrt(number)), 2):
            if number % x == 0:
                primes.append(x)

    n += 1
    number += n

    if n % 100000 == 0 or n % 1000000 == 0 or n % 10000 == 0:
        print(number)


print(count)


# answer = 76 000 000 no se cuantos





