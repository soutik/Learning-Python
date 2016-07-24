# Method 1: Recurssion (Time Complexity O(a^n): Exponential)
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
        
        
num = input("Enter Number")
num = int(num)

a = []
for i in range(num): 
    a.append(F(i+1))
    
print a

# Method 2: Recurssion (Time Complexity O(a^n): Exponential)
def F1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F1(n-1) + F1(n-2)
    
    
b = []
for i in range(num): 
    b.append(F1(i+1))
    
print b

# Method 3: Iteration (Time Complexity O(n): Linear)
def F3(num):
    fib = [1,1]
    a = 2
    b = range(num+1)
    for i in b[3:]:
        a = a + fib[i-1] +fib[i-2]
        fib.append(a)
    return fib

c = []
c.append(F3(num))
print c
            