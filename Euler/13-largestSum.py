runningTotal = 0

file = open('13-largestSum.dat', 'r')
lines = file.readlines()

for line in lines:
        number = int(line.strip())
        runningTotal += number

newTotal = str(runningTotal)
print(newTotal[:10])
    

