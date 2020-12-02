import time
start_time = time.time()

datafile = 'data/day02.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

def isPasswordValidPart1(pw, c, min, max):
    count = len(pw.split(c))-1
    return (min <= count and count <= max)

def isPasswordValidPart2(pw, c, pos1, pos2):
    t = pw[pos1-1] + '' + pw[pos2-1]
    return (1 == len(t.split(c))-1)



part1Count = 0
part2Count = 0
for x in values:
    temp = x.split(" ")
    p = temp[2]
    c = temp[1][0]
    mn, mx = temp[0].split("-")
    if (isPasswordValidPart1(p, c, int(mn), int(mx))):
        part1Count += 1
    if (isPasswordValidPart2(p, c, int(mn), int(mx))):
        part2Count += 1
    
print("Part 1: %s" % part1Count)
print("Part 2: %s" % part2Count)

print("--- %s seconds ---" % (time.time() - start_time))