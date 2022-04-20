
def myFunc(num):
    count = 1
    while(num != 1):
        if num %2 == 0:
            num = num/2
            count +=1
        elif num %2 != 0:
            num = (num*3)+1
            count +=1
    return count
highest = [0,0]
for x in range(1, 1000000):
   if myFunc(x) > highest[1]:
       highest = [x, myFunc(x)]
print(highest)
