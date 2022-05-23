# PROBLEM 11
import numpy as np

with open("p11.txt", "r") as file:
    lines = file.readlines()

numbers = [line.strip().split() for line in lines]
matriz = np.array([[int(n) for n in fila] for fila in numbers])

# # Priemero comprobamos en que direccion esta. Descartamos horizontal y vertical

# R = 20
# C = 20
# maximo = 0
 
 
# def isValid(i, j):
#     if (i < 0 or i >= R or j >= C or j < 0):
#         return False
#     return True

# # horizontal

# for i in range(20):
#     for j in range(20):
#         producto = 1
#         for k in range(j, j+4):
#             if isValid(i, k):
#                 producto *= matriz[i][k]

#         if producto > maximo:
#             maximo = producto

# # vertical

# for j in range(20):
#     for i in range(20):
#         producto = 1
#         for k in range(j, j+4):
#             if isValid(i, k):
#                 producto *= matriz[j][k]

#         if producto > maximo:
#             maximo = producto

# print(maximo) 
# answer = 48477312


# digagonal 
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

# The syntax a[slice,slice] returns a new array with elements from the sliced ranges,
# where "slice" is Python's [start[:stop[:step]] format.

# "::-1" returns the rows in reverse. ":" returns the columns as is,
# effectively vertically mirroring the original array so the wanted diagonals are
# lower-right-to-uppper-left.

diagonales = [matriz[::-1,:].diagonal(i) for i in range(-19, 20)]

# Now back to the original array to get the upper-left-to-lower-right diagonals,
# starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.

diagonales.extend(matriz.diagonal(i) for i in range(-19, 20))


# convert to a normal list
diags = [n.tolist() for n in diagonales]

maximo = 0

for arr in diagonales:
    if len(arr) >= 4:
        for i in range(len(arr)):
            producto = 1
            if i + 4 <= len(arr):
                for j in range(i, i + 4):
                    producto *= arr[j]

            if producto > maximo:
                maximo = producto
                
        

print(maximo)

# expected answer: 70600674




 