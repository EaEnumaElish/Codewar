def reverseSymbols(string):
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
  

string = "{([()])}"
print(string)

print(reverseSymbols(string))
