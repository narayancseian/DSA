from collections import deque
 
 
class MinStack:
    def __init__(self):
        # main stack to store elements
        self.s = deque()
        # variable to store the minimum element
        self.min = None
 
    # Inserts a given element on top of the stack
    def push(self, val):
        if not self.s:
            self.s.append(val)
            self.min = val
        elif val > self.min:
            self.s.append(val)
        else:
            self.s.append(2*val - self.min)
            self.min = val
 
    # Removes the top element from the stack
    def pop(self):
        if not self.s:
            self.print('Stack underflow!!')
            exit(-1)
        top = self.s[-1]
        if top < self.min:
            self.min = 2*self.min - top
        self.s.pop()
 
    # Returns the minimum element from the stack in constant time
    def getMin(self):
        return self.min
 
 
if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(6)
    print(s.getMin())
 
    s.push(7)
    print(s.getMin())
 
    s.push(5)
    print(s.getMin())
 
    s.push(3)
    print(s.getMin())
 
    s.pop()
    print(s.getMin())
 
    s.pop()
    print(s.getMin())
