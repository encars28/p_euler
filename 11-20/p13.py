# PROBLEM 13

with open("p13.txt", "r") as file:
    lines = file.readlines()

numbers = [int(line.strip()) for line in lines]

print(sum(numbers))

