import time
start_time = time.time()

datafile = 'data/day07.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())

bagRules = {}
bagSet = set()

for x in values:
    x = x.replace(" bags", " bag")
    x = x.replace(" bag", "")
    x = x.replace(".", "")
    temp = x.split(" contain ")
    temp[0] = temp[0].replace(" ", "_")
    bagSet.add(temp[0])
    bagRules[temp[0]] = {"bags":[], "counts":[]}
    if(temp[1]!="no other"):
        oTemp = temp[1].split(",")
        for b in oTemp:
            b = b.strip()
            t = b.split(" ")
            u = t[1:]
            v = "_".join(u)
            bagSet.add(v)
            bagRules[temp[0]]["bags"].append(v)
            bagRules[temp[0]]["counts"].append(int(t[0]))
        

def canBagContainGoldBag(bag):
    b = bagRules[bag]
    for x in range(len(b['bags'])):
        if(b['bags'][x] == "shiny_gold" or canBagContainGoldBag(b['bags'][x])):
            return True
    return False

part1 = 0
for bag in bagSet:
    if(canBagContainGoldBag(bag)):
        part1 += 1
        
print("Part 1: %s" % part1)


def getBagCounts(bag):
    count = 0
    temp = bagRules[bag]
    if(len(temp["counts"])!=0):
        count = sum(temp["counts"])
    for x in range(len(temp['bags'])):
        count += temp["counts"][x] * getBagCounts(temp["bags"][x])
    return count

 
print("Part 2: %s" % getBagCounts('shiny_gold'))

print("--- %s seconds ---" % (time.time() - start_time))