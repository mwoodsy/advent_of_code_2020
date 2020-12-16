import time
start_time = time.time()

datafile = 'data/day14.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())


def applyMask(value, mask):
    b = f'{int(value):08b}'
    b = str(b).zfill(36)
    v = list(b)
    for i in range(len(mask)):
        if mask[i] != 'X':
            if mask[i]=="1":
                v[i] = '1'
            elif mask[i] == '0':
                v[i] = '0'
    b = "".join(v)
    value = int(b, 2)
    return value

mask = ''
mem = [0]*100000
for x in data:
    line = x.split(" = ")
    if line[0] == 'mask':
        mask = line[1]
    else:
        index = line[0].replace('mem[','').replace(']','')
        mem[int(index)] = int(applyMask(line[1], mask))

part1 = sum(mem)


print("Part 1: %s" % part1)

import copy
def getAllCombos(value):
    result = []
    value = copy.deepcopy(value)
    if value.count('X') == 0:
        v = "".join(value)
        return [int(v,2)]
    for i in range(len(value)):
        if (value[i]=='X'):
            value[i] = '0'
            result = result + getAllCombos(value)
            value[i] = '1'
            result = result + getAllCombos(value)
    return result

def applyMaskV2(value, mask):
    b = f'{int(value):08b}'
    b = str(b).zfill(36)
    v = list(b)
    for i in range(len(mask)):
        if mask[i] == 'X':
            v[i] = 'X'
        elif mask[i]=="1":
            v[i] = '1'  
    
    combos = getAllCombos(v)
    memlocations = []
    for c in combos:
        memlocations.append(int(c))
    return memlocations

mem2 = {}
for x in data:
    line = x.split(" = ")
    if line[0] == 'mask':
        mask = line[1]
    else:
        memloc = line[0].replace('mem[','').replace(']','')
        indexes = applyMaskV2(memloc, mask)
        for i in indexes:
            mem2["mem"+str(i)] = int(line[1])

part2 = 0
for k, v in mem2.items():
    part2 += int(v) 
print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))