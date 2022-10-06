class Stack:
    # Constructor
    def __init__(self, n):
        self.capacity = n
        self.A = [None] * n
        self.top1 = -1
        self.top2 = n
 
    # Function to insert a given element into the first stack
    def push_first(self, key):
        # check if the list is full
        if self.top1 + 1 == self.top2:
            print('Stack Overflow')
            exit(-1)
        self.top1 = self.top1 + 1
        self.A[self.top1] = key
 
    # Function to insert a given element into the second stack
    def push_second(self, key):
        # check if the list is full
        if self.top1 + 1 == self.top2:
            print('Stack Overflow')
            exit(-1)
        self.top2 = self.top2 - 1
        self.A[self.top2] = key
 
    # Function to pop an element from the first stack
    def pop_first(self):
        # if no elements are left in the list
        if self.top1 < 0:
            print('Stack Underflow')
            exit(-1)
        top = self.A[self.top1]
        self.top1 = self.top1 - 1
        return top
 
    # Function to pop an element from the second stack
    def pop_second(self):
        # if no elements are left in the list
        if self.top2 >= self.capacity:
            print('Stack Underflow')
            exit(-1)
        top = self.A[self.top2]
        self.top2 = self.top2 + 1
        return top
 
 
if __name__ == '__main__':
 
    first = [1, 2, 3, 4, 5]
    second = [6, 7, 8, 9, 10]
 
    stack = Stack(len(first) + len(second))
 
    [stack.push_first(i) for i in first]
    [stack.push_second(j) for j in second]
 
    print('Popping element from the first stack:', stack.pop_first())
    print('Popping element from the second stack:', stack.pop_second())
 
