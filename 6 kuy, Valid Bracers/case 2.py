import flipIt

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




def case_2(originalStr, isOddString):
    if (isOddString % 2 == 0):
        result = True
        parmas = par(isOddString)
        notparmas = notpar(isOddString)
        for i in parmas:
           print(i)



    else:
        result = False
        return result    
    return result


isOddString = 4 
originalStr = '()[]()'
reversedStr = ')(]['
print(case_2(originalStr, isOddString))

