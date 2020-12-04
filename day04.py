import time
start_time = time.time()

datafile = 'data/day04.txt'
with open(datafile) as f:
    values = list(f.read().splitlines())


class Passport:
    def __init__(self):
        self.byr = "" #(Birth Year)
        self.iyr = "" #(Issue Year)
        self.eyr = "" #(Expiration Year)
        self.hgt = "" #(Height)
        self.hcl = "" #Hair Color)
        self.ecl = "" #(Eye Color)
        self.pid = "" #(Passport ID)
        self.cid = "" #(Country ID)

    def clear(self):
        self.byr = "" #(Birth Year)
        self.iyr = "" #(Issue Year)
        self.eyr = "" #(Expiration Year)
        self.hgt = "" #(Height)
        self.hcl = "" #Hair Color)
        self.ecl = "" #(Eye Color)
        self.pid = "" #(Passport ID)
        self.cid = "" #(Country ID)
    def isValid(self):
        valid = True
        valid = valid and (len(self.byr)>0)
        valid = valid and (len(self.iyr)>0)
        valid = valid and (len(self.eyr)>0)
        valid = valid and (len(self.hgt)>0)
        valid = valid and (len(self.hcl)>0)
        valid = valid and (len(self.ecl)>0)
        valid = valid and (len(self.pid)>0)
        #valid = valid and (len(self.cid)>0) #optional
        return valid

    def isExtraValid(self):
        valid = True
        try:
            vByr = (int(self.byr) >= 1920) and (int(self.byr) <= 2002)
            vIyr = (int(self.iyr) >= 2010) and (int(self.iyr) <= 2020)
            vEyr = (int(self.eyr) >= 2020) and (int(self.eyr) <= 2030)
            vHgt = False
            hUnit = self.hgt[-2:]
            if(hUnit == "cm"):
                vHgt = (int(self.hgt[:3]) >= 150) and (int(self.hgt[:3]) <= 193)
            elif(hUnit == "in"):
                vHgt = (int(self.hgt[:2]) >= 59) and (int(self.hgt[:2]) <= 76)
            vHcl = (len(self.hcl) == 7) and (self.hcl[0] == '#') and (int(self.hcl[1:], 16))
            vEcl = self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            vPid = (len(self.pid)==9) and (int(self.pid)>=0)
            valid = valid and vByr
            valid = valid and vIyr
            valid = valid and vEyr
            valid = valid and vHgt
            valid = valid and vHcl
            valid = valid and vEcl
            valid = valid and vPid
        except:
            valid = False
        return valid


p = Passport()
vCount = 0
xCount = 0
for x in values:
    if(x == ""):
        if(p.isValid()):
            vCount+=1
            if(p.isExtraValid()):
                xCount+=1
        p.clear()
    else:
        r = x.split(" ")
        for y in r:
            d = y.split(":")
            s = "p."+d[0]+"='"+d[1]+"'"
            exec(s)

if(p.isValid()):
    vCount+=1
    if(p.isExtraValid()):
        xCount+=1
print("Part 1: %s" % vCount)
print("Part 2: %s" % xCount)

print("--- %s seconds ---" % (time.time() - start_time))