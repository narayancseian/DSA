from collections import deque
 
 
# Implement a queue using two stacks
class Queue:
 
    # Constructor
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
 
    # Add an item to the queue
    def enqueue(self, data):
 
        # Move all elements from the first stack to the second stack
        while len(self.s1):
            self.s2.append(self.s1.pop())
 
        # push item into the first stack
        self.s1.append(data)
 
        # Move all elements back to the first stack from the second stack
        while len(self.s2):
            self.s1.append(self.s2.pop())
 
    # Remove an item from the queue
    def dequeue(self):
 
        # if the first stack is empty
        if not self.s1:
            print('Underflow!!')
            exit(0)
 
        # return the top item from the first stack
        return self.s1.pop()
 
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
    q = Queue()
 
    # insert above keys
    for key in keys:
        q.enqueue(key)
 
    print(q.dequeue())        # 1
    print(q.dequeue())        # 2
