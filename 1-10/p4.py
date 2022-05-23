# PROBLEM 4

# el maximo numero que sale del producto de dos numeros de dos cifras tiene 6 cifras
# 999*999 = 998.001
# de esta manera el palindromo sera de la forma: xyzzyx
# 9 posibilidades para x * 10 para y * 10 para z = 900 palindromos de 6 cifras

# encontrar todos los polindromos de 3 cifras
numbers = []
for x in range(1, 10):
    for y in range(10):
        for z in range(10):
            n = f"{x}{y}{z}{z}{y}{x}"
            numbers.append(int(n))

# calcular el mayor producto de 3 cifras que este en la lista
max = numbers[1]
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if i * j > max and i * j in numbers:
            max = i * j


print(max)

# OTRAS OPCIONES

# comprobar que es palindromo sin hacer la lista

# function reverse(n)
#   reversed = 0
#   while n > 0
#       reversed = 10*reversed + n mod 10
#       n = n/10
#   return reversed

# function isPalindrome(n)
#   return n = reverse(n)

# largestPalindrome = 0
# a = 999
# while a >= 100
#   b = 999
#       while b >= a
#           if a*b <= largestPalindrome
#               break //Since a*b is always going to be too small
#           if isPalindrome(a*b)
#               largestPalindrome = a*b
#           b = b-1
#       a = a-1
# output largestPalindro

# otra opcion tambien es tener en cuenta que a y b 
# tienen que ser multiplos de 11

# This is fast but can be sped up further with some analysis. Consider the digits
# of P – let them be x, y and z. P must be at least 6 digits long since the
# palindrome 111111 = 143×777 – the product of two 3-digit integers. Since P is
# palindromic:
# P=100000x + 10000y + 1000z + 100z + 10y + x
# P=100001x + 10010y + 1100z
# P=11(9091x + 910y + 100z)
# Since 11 is prime, at least one of the integers a or b must have a factor of 11.
# So if a is not divisible by 11 then we know b must be

# https://projecteuler.net/overview=004