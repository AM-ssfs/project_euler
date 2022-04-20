import random
#In a room N chairs are placed around a round table.
#Knights enter the room one by one and choose at random an available empty chair.
#To have enough elbow room the knights always leave at least one empty chair between each other.

#When there aren't any suitable chairs left, the fraction C of empty chairs is determined.
#We also define E(N) as the expected value of C.
#We can verify that E(4) = 1/2 and E(6) = 5/9.

#Find E(10^18). Give your answer rounded to fourteen decimal places in the form 0.abcdefghijklmn.

#1 = 0
#2 = 1/2
#3 = 2/3
#4 = 1/2
#5 = 3/5
#6 = 5/9
#7 = 4/7
#8 = 0.5666666663


#chairs = 10^18

# "-" = empty okay chair, "x" empty invalid chair, "o" = occupied chair

def somethingCrazy():
    chairs = []
    for x in range(6):
        chairs.append("-")

    for x in range(10): # THIS WILL BREAK LATER only placing 10
        randChair = random.randint(0, chairs.count("-"))
        tempChairs = chairs

        myVar = 0
        while randChair-1 > 0:

            if tempChairs[myVar] == "-":
                tempChairs[myVar] = "n"
                randChair -= 1

            myVar += 1

        if "-" in tempChairs:
            chairChoice = tempChairs.index("-")
        while "n" in tempChairs:
            tempChairs[tempChairs.index("n")] = "-"


        print(chairs)
        chairs[chairChoice] = "o"
        chairs[chairChoice-1] = "x"
        if chairChoice+1 < len(chairs):
            chairs[chairChoice+1] = "x"
        else:
            chairs[0] = "x"
    print(chairs)
    return (chairs.count("x"))


total = []
for x in range(0,10000):
    total.append(somethingCrazy())

print(total.count(4))
print(total.count(3))
print(sum(total)/len(total)/6) # percent of empty chairs
#target value for 6 chairs: 5/9 or 0.555555555555555...6
