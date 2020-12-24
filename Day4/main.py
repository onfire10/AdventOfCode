import re

BIRTH_YEAR_PATTERN = re.compile("^(192[0-9]|19[3-9][0-9]|200[0-2])$")
ISSUE_YEAR_PATTERN = re.compile("^(201[0-9]|2020)$")
EXPIRTAION_YEAR_PATTERN = re.compile("^(202[0-9]|2030)$")
HEIGHT_PATTERN = re.compile("^(59in|6[0-9]in|7[0-6]in|15[0-9]cm|1[6-8][0-9]cm|19[0-3]cm)$")
HAIR_COLOR_PATTERN = re.compile("^#(?:[0-9a-f]{3}){1,2}$")
EYE_COLOR_PATTERN = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")
PASSPORT_ID_PATTERN = re.compile("\d{9}$")
COUNTRY_ID_PATTERN = re.compile(".*")

PASSPORT_KEYS = [   ["byr", BIRTH_YEAR_PATTERN], 
                    ["iyr", ISSUE_YEAR_PATTERN],
                    ["eyr", EXPIRTAION_YEAR_PATTERN],
                    ["hgt", HEIGHT_PATTERN],
                    ["hcl", HAIR_COLOR_PATTERN],
                    ["ecl", EYE_COLOR_PATTERN],
                    ["pid", PASSPORT_ID_PATTERN],
                    ["cid", COUNTRY_ID_PATTERN]
]

DATA = [None]

PART1 = 1
PART2 = 2


def readFromFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    passport = ""
    for line in lines:
        if (len(line.strip())!=0):
            passport += line.rstrip('\n') + " "
        else:
            DATA.append(passport)
            passport = ""
    
    file.close()


def validatePassports(mode):
    totalValidPassports = 0
    for passport in DATA:
        if(passport != None):    
            if (passport.count(":") == len(PASSPORT_KEYS)):
                if(mode == PART1):
                    totalValidPassports += 1
                elif(mode == PART2):
                    if(validateFields(passport)):
                        totalValidPassports += 1
            elif (passport.count(":") == len(PASSPORT_KEYS) - 1):
                if (passport.find(PASSPORT_KEYS[-1][0]) == -1):
                    if(mode == PART1):
                        totalValidPassports += 1
                    elif(mode == PART2):
                        if(validateFields(passport)):
                            totalValidPassports += 1
    
    print(totalValidPassports)


def validateFields(passport):
    fields = passport.split(" ")
    del fields[-1]
    for i in range(0, int(len(PASSPORT_KEYS))):
        index = indexContainingSubstring(fields, PASSPORT_KEYS[i][0])
        attr, value = fields[index].split(":")
        if(PASSPORT_KEYS[i][1].match(value) == None):
            return False       
    
    return True

def indexContainingSubstring(fields, key):
    for i, s in enumerate(fields):
        if key in s:
            return i
    return -1


def main():
    readFromFile("day4Input.txt")
    validatePassports(PART2)

if __name__ == "__main__":
    main()