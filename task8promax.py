def cheaser(x):
    if x == '': 
        return x
    let = ord(x[0])
    
    if let == 122:
        let = 96
    res = chr(let + 1)
    
    x = x[1:]
    
    if len(x) == 0:
        return res
    else:
        return res + cheaser(x)
    
print(cheaser(input()))