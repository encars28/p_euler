# PROBLEM 6

# informacion sobre la formula y demostraciones https://www.cuemath.com/algebra/sum-of-squares/
# SUM = 12 + 22 + 32 + ... + n2 = [n(n+1)(2n+1)] / 6. 

print(sum([n for n in range(1, 101)])*sum([n for n in range(1, 101)]) - (int((100*(100+1)*(2*100+1)) / 6)))

# https://projecteuler.net/overview=006