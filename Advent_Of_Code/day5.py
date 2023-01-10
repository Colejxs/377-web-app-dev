moves = []


stacks = initializeStacks()

def initializeStacks():
    #Snipiet
    return [ ['Z', 'N' ], ['M', 'C', 'D'], ['P']]



def loadData():
    global moves 

    file = open('day5.dat', 'r')
    lines = file.readlines()

    instructions = False

    for line in lines:
        line = line.strip()
        if(instructions):
            #split is based on space 
            pieces = line.split()
            moveCount = int(pieces[1])
            moveFrom = int(pieces[3]) - 1
            moveTo = int(pieces[5]) -  1
            moves.append([moveCount, moveFrom, moveTo])
        elif(line == ''):
            instructions = False


def part1(): 
    count = 0

    for move in moves:
        moveCount = move[0]
        moveFrom = move[1]
        move

