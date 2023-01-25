palindromes = []
def checkPalindrome(num):
    num = str(num)
    length = len(num) / 2
    length = int(length)
    firstHalf = num[:length]
    secondHalf = num[-length:]
    reversedSecond = secondHalf[::-1]
    if(firstHalf == reversedSecond):
        palindromes.append(int(firstHalf + secondHalf))


for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        palindrome = checkPalindrome(num)


palindromes.sort()
print(palindromes[-1])
