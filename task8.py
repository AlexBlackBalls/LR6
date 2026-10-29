def cheser(x, i=0) -> str: 
    if i == len(x):
            return ''
    if x[i] == 'z':
        let_new = 'a'
    else:
        alet = ord(x[i])
        alet_new = alet + 1 
        let_new = chr(alet_new)
    return let_new + cheser(x, i + 1)

print(cheser(input()))
    
    
