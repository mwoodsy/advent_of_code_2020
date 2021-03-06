import time
start_time = time.time()

datafile = 'data/day06.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

questionaire = [0]*26
qSum1 = 0
qSum2 = 0
groupMembers = 0
for q in values:
    if (q == ""):
        qSum1 += 26 - questionaire.count(0)
        qSum2 += questionaire.count(groupMembers)
        questionaire = [0]*26
        groupMembers = 0
    else:
        groupMembers += 1
        for a in q:
            i = ord(a) - 97
            questionaire[i] += 1 
    
qSum1 += 26 - questionaire.count(0)
qSum2 += questionaire.count(groupMembers)


print("Part 1: %s" % qSum1)
print("Part 2: %s" % qSum2)

print("--- %s seconds ---" % (time.time() - start_time))