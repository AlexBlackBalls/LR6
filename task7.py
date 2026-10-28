def con(s, char="а", i=0):
    if i == len(s):
        return 0
    return (s[i] == char) + con(s, char, i + 1)

print(con(input()))  