# Exercise 15

def backward(entry):
    process = entry.split()
    rev = []

    i = len(process) - 1
    while i > -1:
        rev.append(process[i])
        i -= 1
    return rev

print(backward(input("Enter a string: ")))