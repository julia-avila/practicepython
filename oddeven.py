# Exercise 2

def checker(num):
    out = ''
    
    if num % 4 == 0:
        out += "Even and a multiple of 4\n"
    elif num % 2 == 0:
        out += "Even\n"
    else:
        out += "Odd\n"
    return out

def divider(num, check):
    out = ''
    
    if num % check == 0:
        out += "Divides evenly"
    else:
        out += "Has modulo"
    return out

a = int(input("Enter a number: "))
print(checker(a))
b = int(input("Enter another number: "))
print(divider(a, b))