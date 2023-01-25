# startingNum = 2050

# i = 0
# while i < 20:
#     print('here')
#     i = 0
#     for i in range(1, 21):
#         if(startingNum % i == 0):
#             print('is multiple')
#             print(i)
#             i += 1
#     startingNum += 1
# print(startingNum)


    
startingNum = 2520

def checkDivis(num):
    for i in range (2, 21):
        if num % i != 0:
            return False
    return True

while True:
    if checkDivis(startingNum):
        break
    startingNum = startingNum + 1 

print(startingNum)
    
