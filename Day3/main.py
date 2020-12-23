FILE_LENGTH = 323
A = [None] * FILE_LENGTH
TREE = "#"

def readFromFile(filename):
    file = open(filename, "r")
    for i, line in enumerate(file):
        A[i] = line.rstrip('\n')
    file.close()

def readArray(right, down):
    lineLength = len(A[0])
    treesCount = 0
    
    j = right
    for i in range(down, int(len(A)), down):
        if(isTree(A[i][j])):
            treesCount = treesCount + 1
        j = j + right
        if(j >= lineLength):
            j = j % lineLength
    
    return treesCount

def isTree(location):
    if(location == TREE):
        return True
    else:
        return False    

def main():
    readFromFile("day3Input.txt")
    inputs = ["1-1" , "3-1" , "5-1" , "7-1" , "1-2"]  
    totalTrees = 1
    for i in range(0, int(len(inputs))):
        right, down = inputs[i].split("-")
        totalTrees = totalTrees * int(readArray(int(right), int(down)))
    print("Solution for Part 2: " + str(totalTrees))


if __name__ == "__main__":
    main()