fib1 = 1
fib2 = 1
tempNum = 0
for x in range(3, 100000):
    tempNum = fib1 + fib2
    fib1 = fib2
    fib2 = tempNum
    if (str(fib2).count("") - 1) == 1000:
        print(x)
        break

print(fib2)
str(tempNum).count("")-1
