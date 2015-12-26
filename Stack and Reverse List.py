class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self)]
        
    def size(self):
        return len(self.items)


# Reversing string by using Stacks
def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
      myStack.push(ch)
    revstr = ''
    while not myStack.isEmpty():
      revstr = revstr + myStack.pop()
    
    return revstr
      
    
print(revstring('apple'))
print(revstring('soutik'))


#Checking balanced parantheses using Stacks
def checkParam(myStr):
    open = Stack()
    balanced = True
    index = 0
    while index < len(myStr) and balanced:
        symbol = myStr[index]
        if symbol == "(":
            open.push(symbol)
        else:
            if open.isEmpty():
                balanced = False
            else:
                open.pop()            
        
        index = index + 1
        
    if balanced and open.isEmpty():
        return True
    else: 
        return False

print(checkParam('((()))'))
print(checkParam('(()'))

        


