import time
start_time = time.time()

datafile = 'data/day12.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

orientation = 90
x,y = 0,0
waypoint=[1, 10, 0 , 0] # N,E,S,W
x2,y2 = 0,0
i = 0
for m in data:
    i += 1
    action = m[0]
    move = int(m[1:])
    if action == 'L':
        orientation = (360 + orientation - move)% 360
        rotate = int(move / 90) 
        waypoint = waypoint[rotate:]+waypoint[:rotate]
    elif action == 'R':
        orientation = (orientation + move) % 360
        rotate = int(move / 90) * -1
        waypoint = waypoint[rotate:]+waypoint[:rotate]
    elif action == "N":
        waypoint[0] += move
        y += move
    elif action == "E":
        waypoint[1] += move
        x += move
    elif action == "S":
        waypoint[2] += move
        y -= move
    elif action == "W":
        waypoint[3] += move
        x -= move
    elif action =="F":
        x2 += move * (waypoint[1] - waypoint[3]) 
        y2 += move * (waypoint[0] - waypoint[2]) 
        if orientation == 0:
            y += move
        elif orientation == 90:
            x += move
        elif orientation == 180:
            y -= move
        elif orientation == 270:
            x -= move

part1 = abs(x)+abs(y)
part2 = abs(x2)+abs(y2)
print("Part 1: %s" % part1)
print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))