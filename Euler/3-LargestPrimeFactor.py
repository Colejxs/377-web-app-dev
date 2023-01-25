# import math
# num = 600851475143
# limit = math.ceil(math.sqrt(num))
# largestPrimeNum = 0
# for i in range(limit):
#     if(not((i % 2 == 0) or (i % 3 == 0) or (i  % 5 == 0))):
#         if (num % i == 0 ):
#             largestPrimeNum = i
# print(largestPrimeNum)

primeFactor = 1
i = 2
num = 600851475143

while i <= num / i:
    if num % i == 0:
        primeFactor = i
        num /= i
    else:
        i += 1

    if primeFactor < num: 
        primeFactor = int(num)


print(primeFactor)