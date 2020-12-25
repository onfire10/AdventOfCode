import collections

DATA = [None]

PART1 = 1
PART2 = 2

def readFromFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    questionsInGroup = ""
    persons = 0
    for line in lines:
        if (len(line.strip())!=0):
            questionsInGroup += line.rstrip('\n')
            persons += 1
        else:
            DATA.append([questionsInGroup, persons])
            questionsInGroup = ""
            persons = 0
    
    file.close()

def getAmountYes(mode):
    amountYes = 0
    for group in DATA:
        if(group != None):
            countIndividualAnswers = collections.Counter(group[0])
            if(mode == PART1):
                amountYes += len(countIndividualAnswers.items())
            elif(mode == PART2):
                amountYes += sum(value == group[1] for value in countIndividualAnswers.values())
    
    print(amountYes)


def main():
    readFromFile("day6Input.txt")
    getAmountYes(PART2)

if __name__ == "__main__":
    main()