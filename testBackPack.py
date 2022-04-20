dmg = 32
multi = .50
totalDmg = 0

for x in range(1, 32):
    multi += 2.0 # mouse wood
    dmg += 1 # stopwatch
    turnDmg = (dmg * multi) * 2
    totalDmg += turnDmg
    print("turn: " + str(x))
    print("dmg this turn: " + str(turnDmg) + ", total dmg: " + str(totalDmg))
