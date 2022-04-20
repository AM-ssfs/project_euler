# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

triangle = 0
add = 0

def checkDivisors(num):
    print()
    print()
    count = 0
    for x in range(1, num):
        if num % x == 0:
            if (num / x) > x:
                print(x)
                count += 2
            elif (num / x) == x:
                count += 1
                break
            elif (num / x) < x:
                break
    print()
    print(count)
    print()
    return count


100
1-100
2-50
3-33.333
4-25
5-20
6-16.666
7-14.2857143
8-12.5
9-11.1111111
10-10
#once divisor equals or is bigger than the quotient, stop, then multiply by 2

for x in range(0, 100000000):
    add+=1
    triangle += add
    if checkDivisors(triangle) > 500:
        print(triangle)
        break

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
