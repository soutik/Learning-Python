# implementing deque in python
class Deque:
    def __init__(self):
        self.items = []
    def addRear(self, item):
        self.items.insert(0, item)
    def addFront(self, item):
        self.items.append(item)
    def removeRear(self):
        return self.items.pop(0)
    def removeFront(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
        

d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())
    
    


# Create a palindrome checker function

def palindromeCheck(aString):
    adeque = Deque()
    
    for ch in aString:
        adeque.addRear(ch)
    
    equal = True
    
    while adeque.size() > 1 and equal:
        if adeque.removeRear() != adeque.removeFront():
            equal = False
    
    return equal
    
    
print(palindromeCheck("lsdkjfskf"))
print(palindromeCheck("radar"))

