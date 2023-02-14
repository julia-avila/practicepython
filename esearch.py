# Exercise 20

import random

def check(l, n):
    out = ''
    l.sort()
    print(l)

    for e in l:
        if e == n:
            return "Yes! Your number can be found in the array."
    
    return "Sorry, your number cannot be found in the array."

l = []
list_len = random.randint(3,10)

for i in range(list_len):
    x = random.randint(0,20)
    l.append(x)

print(check(l, int(input("Enter a number from 0 to 20: "))))
