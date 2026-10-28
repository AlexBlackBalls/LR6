def palindrome(x):
    x = x.replace(" ", "").lower()
    x1 = x[::-1]
    if x == x1: print("Да")
    else: print("Нет")
    
palindrome(input())