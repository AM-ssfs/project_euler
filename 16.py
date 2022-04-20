#power digit sum, What is the sum of the digits of the number 2^1000?

num = 7^5
numStr = str(num)
numList = []

while(numStr != ""):
    numList.append(numStr[0])
    numStr = numStr[1:]
    print(numList)