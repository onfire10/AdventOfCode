A = [None]

def readFromFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        A.append(line.rstrip('\n').split(":"))
    file.close()


def checkPasswordValidity():
    validPasswordsPart1 = 0
    validPasswordsPart2 = 0
    for i in range(0, int(len(A))):
        if(A[i] != None):
            password = str(A[i][1]).lstrip()
            min, maxAndKey = str(A[i][0]).split("-")
            max, key = maxAndKey.split(" ")
            
            count = int(password.count(key))
            if(count >= int(min) and count <= int(max)):
                validPasswordsPart1 = validPasswordsPart1 + 1

            if(isValidforPart2(password, key, int(min)-1, int(max)-1)):
                validPasswordsPart2 = validPasswordsPart2 + 1
                
    print("Solution to Part 1: " + str(validPasswordsPart1))
    print("Solution to Part 2: " + str(validPasswordsPart2))  


def isValidforPart2(password, key, firstIndex, secondIndex):
    if(password[firstIndex] == key):
        if(password[secondIndex] != key):
            return True
    else:
        if(password[secondIndex] == key):
            return True
    return False


def main():
    readFromFile("day2Input.txt")
    checkPasswordValidity()


if __name__ == "__main__":
    main()