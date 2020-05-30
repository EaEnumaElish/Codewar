def wave(people):
    new = []
    for i, val in enumerate(s[:]):
        up = people[i].upper()
        c = people[:i] + up + s[i+1:]
        new.append(c)
    return new






s = 'hello'
print(wave(s))