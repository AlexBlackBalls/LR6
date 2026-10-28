def length(x):
    if len(x) < 5: print("Короткая")
    elif 5 <= len(x) <= 10: print("Средняя")
    else: print("Длинная")
    
length(input())