from collections import deque
 
 
class MinStack:
    # constructor
    def __init__(self):
        # main stack to store elements
        self.s = deque()
        # auxiliary stack to store minimum elements
        self.aux = deque()
 
    # Inserts a given element on top of the stack
    def push(self, val):
        # push the given element into the main stack
        self.s.append(val)
 
        # if the auxiliary stack is empty, push the given element into it
        if not self.aux:
            self.aux.append(val)
        else:
            # push the given element into the auxiliary stack
            # if it is less than or equal to the current minimum
            if self.aux[-1] >= val:
                self.aux.append(val)
 
    # Removes the top element from the stack and returns it
    def pop(self):
        if self.isEmpty():
            print('Stack underflow')
            exit(-1)
 
        # remove the top element from the main stack
        top = self.s.pop()
 
        # remove the top element from the auxiliary stack
        # only if it is minimum
        if top == self.aux[-1]:
            self.aux.pop()
 
        # return the removed element
        return top
 
    # Returns the top element of the stack
    def top(self):
        return self.s[-1]
 
    # Returns the total number of elements in the stack
    def size(self):
        return len(self.s)
 
    # Returns true if the stack is empty; false otherwise
    def isEmpty(self):
        return not self.s
 
    # Returns the minimum element from the stack in constant time
    def getMin(self):
        if not self.aux:
            print('Stack underflow')
            exit(-1)
        return self.aux[-1]
 
 
if __name__ == '__main__':
 
    s = MinStack()
 
    s.push(6)
    print(s.getMin())        # prints 6
 
    s.push(7)
    print(s.getMin())        # prints 6
 
    s.push(8)
    print(s.getMin())        # prints 6
 
    s.push(5)
    print(s.getMin())        # prints 5
 
    s.push(3)
    print(s.getMin())        # prints 3
 
    print(s.pop())          # prints 3
    print(s.getMin())        # prints 5
 
    s.push(10)
    print(s.getMin())        # prints 5
 
    print(s.pop())          # prints 10
    print(s.getMin())        # prints 5
 
    print(s.pop())          # prints 5
    print(s.getMin())        # prints 6
