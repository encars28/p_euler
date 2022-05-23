# PROBLEM 18

# ver la estructura del triangulo en el documento de texto (colocado como triangulo rectangulo)
# Lo que quiero es ir eligiendo el mayor numero desde arriba y elegir entre los dos 
# que tiene inmediatamente debajo cual es el mayor, para ir haciendo el camino

# al estar el triangulo colocado asi, es facil de ver que los numeros que hay
# que comprobar son el que esta debajo y el de la derecha de este


# cargo los numeros

with open("p18.txt", "r") as f:
    lines = f.readlines()

triangle = [line.split() for line in lines]
triangle = [[int(n) for n in line] for line in triangle]

# voy comprobando cual es mayor

# tengo q mirar que es mas grande, si la suma de el numero con elo de abajo mas grande
# o la suma del otro numero con el de abajo
path = [triangle[0][0]]
j = 0

for i in range(0, len(triangle)):
    if i < len(triangle) - 2:
        if triangle[i + 2][j] > triangle[i + 2][j + 1]: max1 = triangle[i + 2][j]
        else: max1 = triangle[i + 2][j + 1]

        if triangle[i + 2][j + 1] > triangle[i + 2][j + 2]: max2 = triangle[i + 2][j + 1]
        else: max2 = triangle[i + 2][j + 2]

        if (max1 + triangle[i + 1][j]) > (max2 + triangle[i + 1][j + 1]):
            path.append(triangle[i + 1][j])
        else:
            path.append(triangle[i + 1][j + 1])
            j +=1
        
    if i == len(triangle) - 2:
        if triangle[i + 1][j] > triangle[i + 1][j + 1]:
            path.append(triangle[i + 1][j])
        else:
            path.append(triangle[i + 1][j + 1])

print(sum(path))

