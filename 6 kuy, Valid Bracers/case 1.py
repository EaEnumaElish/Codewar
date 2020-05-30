#case 1
#([]) originalStr
#)][( reversedStr
import flipIt
import reverseSym




def case_1(originalStr, reversedStr, isOddString):
    for i in range(isOddString):
        if (originalStr[0 + i] == flipIt.flipSym(reversedStr[0 + i])):
            result = True
        elif (originalStr[0 + i] != flipIt.flipSym(reversedStr[0 + i])):
            result = False
        else:
            pass
    return result


isOddString = 4 
originalStr = '(({{[[]]}}))'
reverseStr = reverseSym.reverseSymbols(originalStr)
print(case_1(originalStr, reverseStr ,isOddString))