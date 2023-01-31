import math
primes = [2]
# for i in range (3, 10002):
#     for j in range(2, i):

#         if i % j == 0:
#             #is not a prime factor 
#             continue
#         else:
#             primes.append(i)

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

i = 3
while len(primes) < 10_001:
    if(isPrime(i)):
        primes.append(i)
    i += 2

print(primes[10000])

