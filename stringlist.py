# Exercise 6

inp = input("Enter a string: ")

if inp.lower() == inp[::-1].lower():
    print("Palindrome")
else:
    print("Not a palindrome")