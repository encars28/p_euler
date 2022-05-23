# PROBLEM 5

# 5 * 7 * 9 * 11 * 13 * 16 * 17 * 19
# como los numeros pueden ser expresados en producto de otros, para que 
# sea divisible entre todos los numeros del 1 al 20, el numeroe estara
# formado por el producto de ellos.
# Sin embargo, solo consideraremos la mayor potencia de los primos involiucrados
# porque el resto de numeros se pueden hacer con combinaciones de ellos

# lo he hecho a mano porque los primos del 1 al 20 son faciles de encontrar

print(5 * 7 * 9 * 11 * 13 * 16 * 17 * 19)

# algoritmo para numeros mas grandes

# For a given p[i] we can determine a[i] in the following way.
# Let p[i]^a[i] = k. By “logging” both sides: a[i] log(p[i]) = log(k).
# So a[i] = log(k) / log(p[i]).
# But as a[i] must be integer, a[i] = floor( log(k) / log(p[i]) ).
# For example, when k = 20, the exponent of the first primes factor, p[1] = 2, will be:
# a[1] = floor( log(20) / log(2) ) = floor( 4.32...) = 4
# To optimise the approach even further we note that a[i] = 1 for p[i]^2 > k. In other
# words, we only need to evaluate a[i] for p[i] ≤ sqrt(k).
# To put all this together into an algorithm we shall assume that an array of primes p[1],
# p[2], p[3], ... has already been created

# https://projecteuler.net/overview=005