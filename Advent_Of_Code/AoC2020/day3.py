# def imSleepy(x, y, ):
#     file = open('day3.dat', 'r')
#     lines = file.readlines()

#     treeCounter = 0
#     index = 0

#     for line in lines:
#         line = line.strip()
#         lineLen = len(line)
        
#         if(index >= lineLen):
#             index = index % lineLen

#         if(line[index] == "#"):
#             treeCounter += 1

#         index += 3
        
#     print(treeCounter)
# imSleepy()



def calTrees(x, y):
    file = open('day3.dat', 'r')
    lines = file.readlines()

    treeCounter = 0
    Xindex = 0
    Yindex = 0

    for line in lines:

        if(Yindex % y == 0):

            line = line.strip()
            lineLen = len(line)
            
            if(Xindex >= lineLen):
                Xindex = Xindex % lineLen

            if(line[Xindex] == "#"):
                treeCounter += 1

            Xindex += x
        Yindex += 1

    return(treeCounter)

print(calTrees(3,1))


print(calTrees(1,1))
print(calTrees(3,1))
print(calTrees(5,1))
print(calTrees(7,1))
print(calTrees(1,2))


print(calTrees(1, 1) * calTrees(3, 1) * calTrees(5, 1) * calTrees(7, 1) * calTrees(1, 2))


