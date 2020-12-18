import time
start_time = time.time()

datafile = 'data/day16.txt'
with open(datafile) as f:
    data = list(f.read().splitlines())

class Field:
    def __init__(self, name, minRange, maxRange):
        self.name = name
        self.minRange = minRange.split('-')
        self.maxRange = maxRange.split('-')
    def couldBeValid(self, num):
        minLow = int(self.minRange[0])
        minHigh = int(self.minRange[1])
        maxLow = int(self.maxRange[0])
        maxHigh = int(self.maxRange[1])
        valid = False
        if (minLow <= num <= minHigh)or(maxLow <= num <= maxHigh):
            valid = True
                
        return valid

rules = []
nearByTickets = []
yourTicket = []
section = "rules"       
for x in data:
    if x == "":
        if section == "rules":
            section = "yourTicket"
        elif section == "yourTicket":
            section = "nearbyTickets"
    elif section == "rules":
        r = x.split(": ")
        n = r[0]
        r = r[1].split(' or ')
        f = Field(n,r[0],r[1])
        rules.append(f)
    elif section == "yourTicket":
        if x != "your ticket:":
            n = x.split(',')
            yourTicket = [int(i) for i in n]
    elif section == "nearbyTickets":
        if x != "nearby tickets:":
            n = x.split(',')
            nearByTickets.append([int(i) for i in n])
            

invalidNumbers = []
validTickets = []
for t in range(len(nearByTickets)):
    ticketValid = True
    for n in range(len(nearByTickets[t])):
        valid = False
        for r in rules:
            valid = valid or r.couldBeValid(nearByTickets[t][n])
        if not valid:
            invalidNumbers.append(nearByTickets[t][n])
            ticketValid = False
    if ticketValid:
        validTickets.append(nearByTickets[t])
        

part1 = sum(invalidNumbers)  
print("Part 1: %s" % part1)


ticketCol = [[validTickets[j][i] for j in range(len(validTickets))] for i in range(len(validTickets[0]))] 

stop = False

fieldValuesByIndex = []
for i in range(len(rules)):
    fieldValuesByIndex.append([])
for r in rules:
    i = 0
    for x in ticketCol:
        valid = True
        for y in x:
            valid = valid and r.couldBeValid(y)
        if(valid):
            fieldValuesByIndex[i].append(r.name)
        i += 1
    
        
while True:
    keepGoing = False
    for f1 in fieldValuesByIndex:
        if len(f1) == 1:
            for i in range(len(fieldValuesByIndex)):
                if f1!=fieldValuesByIndex[i] and f1[0] in fieldValuesByIndex[i]:
                    fieldValuesByIndex[i].remove(f1[0])
    for f in fieldValuesByIndex:
        if len(f)>1:
            keepGoing = True
    if not keepGoing:
        break
depts = []
for i in range(len(fieldValuesByIndex)):
    temp = str(fieldValuesByIndex[i])
    if 'departure' in temp:
        depts.append(i)
part2 = 1
for x in depts:
    part2 *= yourTicket[x]

print("Part 2: %s" % part2)

print("--- %s seconds ---" % (time.time() - start_time))