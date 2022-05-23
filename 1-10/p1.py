# PROBLEM 1
suma = 0

for x in range(0, 1000):
    if x % 3 == 0 or x % 5 == 0:
        suma += x

print(suma)

# OTRAS OPCIONES

# para que sea mas eficiente tambien se podia hacer calculando los divisbles entre 3,
# los divisibles entre 5, sumandolos y luego restandoles los divisibles entre 15
# se puede hacer facil con una funcion divisibleby(n)

# https://projecteuler.net/overview=001

    









