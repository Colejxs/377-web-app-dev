for i in range (2, 10):
    for j in range(i):
        if i % j == 0:
            #is not a prime factor 
            break
        else:
            print(i)