A = [None] *200
TARGET = 2020

def readFromFile(filename):
    file = open(filename, "r")
    for i, line in enumerate(file):
        A[i] = int(line)
    file.close()

def checkPart1():
    for i in A:
        for j in A:
            if i + j == TARGET:
                print("Solution to Part 1: " + str(i*j))
                return

def checkPart2():
    for i in A:
        for j in A:
            for k in A:
                if i + j + k == TARGET:
                    print("Solution to Part 2: " + str(i*j*k))
                    return

def main():
    readFromFile("day1Input.txt")
    checkPart1()
    checkPart2()

if __name__ == "__main__":
    main()