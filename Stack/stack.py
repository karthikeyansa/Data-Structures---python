class Stack:
    def __init__(self):
        self.stack=[]
    def add (self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False#add is not used here
    def peek():
        return self.stack[-1]
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def remove(self):
        if len(self.stack)<=0:
            return 'no element'
        else:
            return self.stack.pop()
    def print(self):
        print( self.stack)
s=Stack()
s.push(4)
s.push(5)
s.push(6)
s.print()
