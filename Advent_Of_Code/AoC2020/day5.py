
def ConvertBin(arr):
    binRow = ""
    #find the row
    for i in range(len(arr)):
        if arr[i] == 'F' or arr[i] == 'L':
            binRow += '0'
        elif arr[i] == 'B' or arr[i] == 'R':
            binRow += '1'
    #print(binRow)
    decRow = int(binRow, 2)
    return(decRow)

def part1():

    file = open('day5.dat', 'r')
    lines = file.readlines()
    highestID = 0
    seats = []
    

    for line in lines:
        line = line.strip()
        row = line[:7]
        column = line[7:]
        

        rowNum = ConvertBin(row)
        columnNum = ConvertBin(column)  
        seatID = (rowNum * 8 ) + columnNum
        seats.append(seatID)
        

        if seatID > highestID:
            highestID = seatID
    
    seats.sort()
    for i in range(len(seats)):
        if seats[i] + 1 != seats[i + 1]:
            print(seats[i])
            break
    print(highestID)
               
part1()


