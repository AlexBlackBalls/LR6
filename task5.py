def rep(x):
    if "a" in x:
        x = x.replace("a", "@")
        print(x)
    else: print(x)
    
rep(input())