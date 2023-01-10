def part1():
     file = open('day2.dat', 'r')
     lines = file.readlines()

     validPWS = 0 


     for line in lines:
        line = line.strip()
        split = line.split(" ")

        criteria = split[0].split("-")
        getletter = split[1][0]

        PW = split[2]
        letterCount = 0

        for i in PW:
            if(getletter == i):
                letterCount += 1
        if(letterCount >= int(criteria[0]) and letterCount <= int(criteria[1])):
            validPWS += 1
        
                
     print(validPWS)

part1()


