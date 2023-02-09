# Exercise 1

name = input("Enter your name:\n")
age = int(input("Enter your age:\n"))
hundred = (2023 - age) + 100
repeat = int(input("Enter a number:\n"))

for i in range(repeat):
    print("Hello " + name + ", you will turn 100 in the year " + str(hundred))