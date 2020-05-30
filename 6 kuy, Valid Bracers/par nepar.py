isOddString = 10

r1 = [i for i in range(isOddString + 1)]




def par(isOddString):
    solve= [0]
    for i in range(isOddString + 1):
        if i == 0:
            pass
        elif i % 2 == 0:
            solve.append(i)
    return solve

def notpar(isOddString):
    solve= []
    for i in range(isOddString + 1):
        if i == 0:
            pass
        elif i % 2 != 0:
            solve.append(i)    
    return solve


print(par(isOddString))
print(notpar(isOddString))


