# PROBLEM 2

fib = [0, 1]
while  fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])

suma = sum([fib[i] for i in range(0, len(fib), 3)])

print(suma)

# OTRAS OPCIONES

# There is another beautiful structure hidden beneath this problem:
# If we only write the even numbers:
# 2 8 34 144...
# it seems that they obey the following recursive relation: E(n)=4*E(n-1)+E(n-2).
# If we can prove that for the Fibonacci numbers the formula F(n)=4*F(n-3)+F(n-6) holds we
# have proven this recursion

# https://projecteuler.net/overview=002
