import time
start_time = time.time()

datafile = 'data/day08.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

acc = 0
i = 0
seen = []
while True:
    seen.append(i)
    if (len(seen)>len(set(seen))):
        break
    instruct = values[i].split(" ")
    if (instruct[0] == "nop"):
        i += 1
    elif (instruct[0] == "acc"):
        acc = acc+eval(instruct[1])
        i += 1
    else:
        i = i + eval(instruct[1])


print("Part 1: %s" % acc)

def nextSwitch(old):
    while old < len(values):
        t = values[old].split(" ")
        if(t[0]=="nop"):
            values[old] = values[old].replace("nop", "jmp")
            break
        elif(t[0]=="jmp"):
            values[old] = values[old].replace("jmp", "nop")
            break
        old += 1
    return old

acc = 0
i = 0
seen = []
old = 0
nextSwitch(old)
while len(seen) < len(values):
    seen.append(i)
    if(i == len(values)):
        break
    if (len(seen)>len(set(seen))):
        nextSwitch(old)
        old = nextSwitch(old+1)
        seen = []
        i = 0
        acc = 0
    instruct = values[i].split(" ")
    if (instruct[0] == "nop"):
        i += 1
    elif (instruct[0] == "acc"):
        acc = acc+eval(instruct[1])
        i += 1
    else:
        i = i + eval(instruct[1])

print("Part 2: %s" % acc)

print("--- %s seconds ---" % (time.time() - start_time))