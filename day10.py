import time
start_time = time.time()

datafile = 'data/day10.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

for x in range(len(data)):
    data[x] = int(data[x])

data.sort()

jolt = 0
diffs = ''
i = 0
while i < len(data):
    jolt = data[i] - jolt
    diffs += str(jolt)
    jolt = data[i]
    i += 1

diffs += '3'

part1 = (diffs.count('1') * (diffs.count("3")))
print("Part 1: %s" % part1)

arr = diffs.replace('13', ' ').replace('3','').strip().split(' ')
part2 = 1
for x in arr:
    if len(x) > 0:
        t = int(x, 2)
        u = 0
        if(len(x)>2):
            u = int(x[:-2],2)
        part2 *= (t + 1)-u

print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))