DATA = [None]
ROWS = 128
COLUMNS = 8
FRONT = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"

SEAT_PLAN = []

def readFromFile(filename):
    file = open(filename, "r")
    for i, line in enumerate(file):
        DATA.insert(i, line.rstrip('\n'))
    del DATA[-1]
    file.close()


def decodeSeats():
    seatId = 0
    for code in DATA:
        rowBinary = ""
        colBinary = ""
        row = 0
        col = 0
        for i in range(0, int(len(code))):
            if(i < 7):
                if(code[i] == BACK):
                    rowBinary += "1"
                elif(code[i] == FRONT):
                    rowBinary += "0"
            else:
                if(code[i] == RIGHT):
                    colBinary += "1"
                elif(code[i] == LEFT):
                    colBinary += "0"
            
        row = binaryToInt(rowBinary)
        col = binaryToInt(colBinary)
        saveSeat(row, col)
        tempSeatID = calculateID(row, col)
        if(tempSeatID > seatId):
            seatId = tempSeatID      
    
    print("Highest Seat-ID: " + str(seatId))
    print("My Seat-ID: " + str(findMySeat()))
                    

def binaryToInt(binary):
    return int(binary, 2)


def calculateID(row, col):
    return row * COLUMNS + col


def saveSeat(row, col):
    SEAT_PLAN.append([row, col])


def findMySeat():
    SEAT_PLAN.sort(key=lambda x: (x[0],x[1]))
    j = 1
    k = 0
    for i in range(0, int(len(SEAT_PLAN))):
        if(SEAT_PLAN[i][0] != 0):
            if(SEAT_PLAN[i][0] != j):
                return calculateID(j, k)
            k += 1
            if(k == 8):
                j += 1
                k = 0


def main():
    readFromFile("day5Input.txt")
    decodeSeats()


if __name__ == "__main__":
    main()