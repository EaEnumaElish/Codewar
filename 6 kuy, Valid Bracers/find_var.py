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





isOddString = 4 
originalStr = '([}{])'
reversedStr = ')(]['
print(find_var(originalStr, isOddString))
