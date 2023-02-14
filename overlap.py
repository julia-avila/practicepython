# Exercise 5

import random

lim1 = random.randint(0,20)
lim2 = random.randint(0,20)
l1 = []
l2 =[]

for i in range(lim1):
    l1.append(random.randint(0,20))

for i in range(lim2):
    l2.append(random.randint(0,20))

l3 = []

for x in l1:
    if x not in l3:
        if x in l2:
            l3.append(x)

print(l1)
print(l2)
print(l3)