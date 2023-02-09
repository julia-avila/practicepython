# Exercise 13

def fibonacci(num):
    number = int(num)
    sum = 0
    final = [1,1]
    for i in range(number):
        sum = final[-2] + final[-1]
        final.append(sum)
    return final[0:(len(final)-2)]

print(fibonacci(input("How many numbers to generate?\n")))