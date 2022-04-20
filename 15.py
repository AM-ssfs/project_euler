
size = 21  # one more than target
across = {}
down = []
across[0] = []
for x in range(size):
    across[0].append(1)
down.append(across[0])


for x in range(1, size):
    across[x] = [1]
    for y in range(1,len(across[0])):
        across[x].append(
            (across[x-1][y]) +
            (across[x][y-1])
        )
    down.append(across[x])

for x in range(size):
    print(down[x])
