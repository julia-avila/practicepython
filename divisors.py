# Exercise 4

num = int(input("Enter a number: "))
divs = []

for i in range(num):
    if i == 0:
        pass
    elif num % i == 0:
        divs.append(i)

print(divs)