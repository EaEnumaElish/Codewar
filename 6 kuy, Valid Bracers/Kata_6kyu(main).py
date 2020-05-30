#reverser of string
def reverseSym(string):
    stringLen = len(string)
    for i in range(stringLen):
        lastSym = string[-1 - i]
        if lastSym == ')':
            lastSym = '('
        elif lastSym == '(':
            lastSym = ')'     
        elif lastSym == ']':
            lastSym = '['  
        elif lastSym == '[':
            lastSym = ']' 
        elif lastSym == '}':
            lastSym = '{'   
        elif lastSym == '{':
            lastSym = '}' 
        string = lastSym + string

    if stringLen % 2 != 0:
        print("Error")
        return False
    else:
        if stringLen == 2:
            string = string[:-2]
            return string
        elif stringLen == 4:
            string = string[:-4]
            return string
        elif stringLen == 6:
            string = string[:-6]
            return string
        elif stringLen == 8:
            string = string[:-8]
            return string
        elif stringLen == 10:
            string = string[:-10]
            return string
        elif stringLen == 12:
            string = string[:-12]
            return string
        elif stringLen == 14:
            string = string[:-14]
            return string
        elif stringLen == 16:
            string = string[:-16]
            return string
        elif stringLen == 18:
            string = string[:-18]
            return string
        elif stringLen == 20:
            string = string[:-20]
            return string
    return string
  
#flipper
def flipIt(sym):
    if sym == ')':
        sym = '('
        return sym
    elif sym == '(':
        sym = ')'
        return sym
    elif sym == ']':
        sym = '['
        return sym
    elif sym == '[':
        sym = ']'
        return sym
    elif sym == '}':
        sym = '{'
        return sym
    elif sym == '{':
        sym = '}'
        return sym

#case 1
def case_1(originalStr, reversedStr, isOddString):
    for i in range(isOddString):
        if (originalStr[0 + i] == flipIt(reversedStr[0 + i])):
            result = True
        elif (originalStr[0 + i] != flipIt(reversedStr[0 + i])):
            result = False
        else:
            pass
    return result

#case 2
def case_2(originalStr, isOddString):
    if (isOddString % 2 == 0):
        result = True
        if (originalStr[0] == flipIt(originalStr[1])):
            result = True
            if (isOddString == 4):
                if (originalStr[2] == flipIt(originalStr[3])):
                    result = True
                    if (isOddString == 6):
                        if (originalStr[4] == flipIt(originalStr[5])):
                            result = True
                            if (isOddString == 8):
                                if (originalStr[6] == flipIt(originalStr[7])):
                                    result = True
                                else:
                                    result = False
                                    return result  
                            else:
                                return result
                        else:
                            result = False
                            return result
                    else:
                        return result
                else:
                    result = False
                    return result
            else:
                return result
        else:
            result = False
            return result
    else:
        result = False
        return result
    return result

#find_var
def find_var(originalStr, isOddString):
    if (isOddString % 2 == 0):
        case_var = 1
        if (originalStr[0] == flipIt(originalStr[1])):
            case_var = 1
            if (isOddString == 4):
                if (originalStr[2] == flipIt(originalStr[3])):
                    case_var = 1
                    if (isOddString == 6):
                        if (originalStr[4] == flipIt(originalStr[5])):
                            case_var = 1
                            if (isOddString == 8):
                                if (originalStr[6] == flipIt(originalStr[7])):
                                    case_var = 1
                                else:
                                    case_var = False
                                    return case_var  
                            else:
                                return case_var
                        else:
                            case_var = False
                            return case_var
                    else:
                        return case_var
                else:
                    case_var = False
                    return case_var
            else:
                return case_var
        else:
            case_var = False
            return case_var
    else:
        case_var = False
        return case_var
    return case_var




# main fun
def validBraces(string):
    result = False
    isOddString = len(string)
    if (isOddString % 2 == 0):
        pass
    else:
        return False
    # which case we are have
    case_var = find_var(string, isOddString)
    # case 1
    if case_var == 1:
        originalStr = string
        reversedStr = reverseSym(string)
        case_1(originalStr, reversedStr, isOddString)
        result = True
    elif case_var == 2:
        originalStr = string
        case_2(originalStr, isOddString)
        result = True

    return result


example = "([}{])"
print(validBraces(example))

