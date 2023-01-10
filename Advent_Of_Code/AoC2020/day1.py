def part1():
    file = open('day1.dat', 'r')
    lines = file.readlines()

    const = 2020
   

    for line in lines:
        #set the numbers into an aray
        currentNum = int(line.strip())
        for num2 in lines:
            if(int(num2.strip()) + currentNum == const):
                answer = int(num2.strip())* currentNum
                break
    

part1()

