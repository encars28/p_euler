# PROBLEM 21

with open("primes.txt", "r") as f:
    primes = f.read().replace("\n", "")
    primes = primes.split("-")
    primes = [int(n) for n in primes]

amicable = []

def sum_divisors(n):
    divisors = [1]
    for p in primes:
        if p >= n: break

        if n % p == 0:
            divisors.append(p)

    return sum(divisors)

# hacer los bucles contando hacia arriba en vez de hacia abajo y guardando las reapuestas como antes?
suma = 0
for i in range(2, 10000):
    for j in range(2, i):
        if sum_divisors(i) == j and sum_divisors(j) == i:
            if i not in amicable:
                amicable.append(i)
                amicable.append(j)

