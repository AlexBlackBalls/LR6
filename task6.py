def name(s):
    n1 = s.find(" ")
    n2 = s.find(" ", n1+1)
    print(f"{s[:n1].capitalize()} {s[n1+1].upper()}.{s[n2+1].upper()}.")
    
name(input())