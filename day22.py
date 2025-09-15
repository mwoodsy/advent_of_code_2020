import time
start_time = time.time()


datafile = 'data/day22.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

player1 = []
player2 = []
p = 0
for d in data:
    if "Player" in d:
        p += 1
    
    elif d != "":
        if p == 1:
            player1.append(int(d))
        elif p == 2:
            player2.append(int(d))

player1.reverse()
player2.reverse()

import copy
game2player1 = copy.deepcopy(player1)
game2player2 = copy.deepcopy(player2)

while len(player1) != 0 and len(player2) != 0:
    p1 = player1.pop()
    p2 = player2.pop()
    if p1 > p2:
        player1.insert(0,p1)
        player1.insert(0,p2)
    else:
        player2.insert(0,p2)
        player2.insert(0,p1)

part1 = 0
for i in range(len(player1)):
    part1 += player1[i]*(i+1)    
for i in range(len(player2)):
    part1 += player2[i]*(i+1)  
print("Part 1:", part1)

player1 = game2player1
player2 = game2player2
print("Part 2:", 2)

print("--- %s seconds ---" % (time.time() - start_time))