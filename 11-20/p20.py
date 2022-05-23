# PROBLEM 20

# https://cs.stackexchange.com/questions/14456/factorial-algorithm-more-efficient-than-naive-multiplication
# https://www.hackerearth.com/practice/notes/efficient-factorials-calculation/

# efficient algorithms, yo lo voy a hacer por lo facil, el recursivo

def fact(n):
    if n == 1 or n == 0:
        return 1

    return n*fact(n - 1)

number = str(fact(100))

print(sum([int(n) for n in number]))