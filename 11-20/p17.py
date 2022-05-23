# PROBLEM 17

def units_to_str(unidades):
    if unidades == 1:
        return "one"
    elif unidades == 2:
        return "two"
    elif unidades == 3:
        return "three"
    elif unidades == 4:
        return "four"
    elif unidades == 5:
        return "five"
    elif unidades == 6:
        return "six"
    elif unidades == 7:
        return "seven"
    elif unidades == 8:
        return "eight"
    elif unidades == 9: 
        return "nine"
    elif unidades == 0:
        return ""

def decens_to_str(decenas, unidades):
    if decenas == 1:
        if unidades == 0:
            return "ten"
        elif unidades == 1:
            return "eleven"
        elif unidades == 2:
            return "twelve"
        elif unidades == 3:
            return "thirteen"
        elif unidades == 4:
            return "fourteen"
        elif unidades == 5:
            return "fifteen"
        elif unidades == 6:
            return "sixteen"
        elif unidades == 7:
            return "seventeen"
        elif unidades == 8:
            return "eighteen"
        elif unidades == 9: 
            return "nineteen"

    elif decenas == 2:
        return ("twenty" + units_to_str(unidades))
    elif decenas == 3:
        return ("thirty" + units_to_str(unidades))
    elif decenas == 4:
        return ("forty" + units_to_str(unidades))
    elif decenas == 5:
        return ("fifty" + units_to_str(unidades))
    elif decenas == 6:
        return ("sixty" + units_to_str(unidades))
    elif decenas == 7:
        return ("seventy" + units_to_str(unidades))
    elif decenas == 8:
        return ("eighty" + units_to_str(unidades))
    elif decenas == 9: 
        return ("ninety" + units_to_str(unidades))
    elif decenas == 0:
        return ""

def centens_to_str(centenas, decenas, unidades):
    if decenas == 0 and unidades == 0:
        return (units_to_str(centenas) + "hundred")
    elif decenas == 0:
        return (units_to_str(centenas) + "hundredand" + units_to_str(unidades))
    else:
        return (units_to_str(centenas) + "hundredand" + decens_to_str(decenas, unidades))


numbers = []
for n in range(1, 1000):
    digits = [int(x) for x in str(n)]

    if len(digits) == 1:
        numbers.append(units_to_str(digits[0]))
    elif len(digits) == 2:
        numbers.append(decens_to_str(digits[0], digits[1]))
    else:
        numbers.append(centens_to_str(digits[0], digits[1], digits[2]))

numbers.append("onethousand")

print(len(("".join(numbers))))