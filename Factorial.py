def fact(num):
    
    if num == 0 | num == 1:
        f = 1
    else:
        f = num * fact(num-1)
    return f
    
print(fact(5))