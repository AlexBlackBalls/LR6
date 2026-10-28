def symb(x):
    if len(x) == 0: 
        print("Строка пуста")
    else: 
        print(f"{x[0]} {x[-1]}")
    
symb(input())
