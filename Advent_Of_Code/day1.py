def part1():
    file = open('day1.dat', 'r')
    lines = file.readlines()

    runningTotal = 0
    max = 0
    count = 0

    for line in lines:
        if (line.strip() == ''):
            if (runningTotal > max):
                max = runningTotal
            runningTotal = 0 
        else:
            number = int(line.strip())
            runningTotal += number

   

    print("part 1: " + str(max))




# day one part 2 

def part2():
    file = open('day1.dat', 'r')
    lines = file.readlines()

    runningTotal = 0
    max = 0
    top3 = []

    for line in lines:
        if (line.strip() == ''):
            top3.append(runningTotal)
            runningTotal = 0 
        else:
            number = int(line.strip())
            runningTotal += number

    top3.sort(reverse=True)
    
    print("part 2: " + str(top3[0]) + " " + str(top3[1]) + " " + str(top3[2]))
    print("part 2: " + str(top3[0] + top3[1] + top3[2]))

    toatal3 = top3[0] + top3[1] + top3[2]
    print(toatal3)

part2()