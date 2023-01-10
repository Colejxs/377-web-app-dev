def part1():
    file = open('day6.dat', 'r')
    line = file.readline().strip()

    print(line)

    for i in range(len(line) - 3):
        chunk = line[i: i + 4]
        print(chunk)
        
        chunkSet = set()
        for c in chunk:
            chunkSet.add(c)
        
        if(len(chunkSet) == 4):
            print(i + 4)
            break

part1()

def findMarker(count):
    file = open('day6.dat', 'r')
    line = file.readline().strip()

    print(line)

    for i in range(len(line) - (count - 1)):
        chunk = line[i: i + count]
        #print(chunk)
        
        chunkSet = set()
        for c in chunk:
            chunkSet.add(c)
        
        if(len(chunkSet) == count):
            print(i + count)
            break

findMarker(14)