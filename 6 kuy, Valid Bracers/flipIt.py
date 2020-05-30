def flipSym(sym):
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