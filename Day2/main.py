A = [None]

def readFromFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        A.append(line.rstrip('\n').split(":"))
    file.close()

def checkPasswordValidity():
    validPasswords = 0
    for i in range(1, int(len(A))):
        password = str(A[i][1])
        min, maxAndKey = str(A[i][0]).split("-")
        max, key = maxAndKey.split(" ")
        
        count = int(password.count(key))
        if(count >= int(min) and count <= int(max)):
            validPasswords = validPasswords + 1
    
    return validPasswords       
            
def main():
    readFromFile("day2Input.txt")
    print(str(checkPasswordValidity()))

if __name__ == "__main__":
    main()