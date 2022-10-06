# A Linked List Node
class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next
 
 
class Stack:
    def __init__(self):
        self.top = None
        self.nodesCount = 0
 
    # Utility function to add an element `x` to the stack
    def push(self, x):        # insert at the beginning
 
        # allocate a new node in a heap
        node = Node(x)
 
        # check if stack (heap) is full. Then inserting an element would
        # lead to stack overflow
        if node is None:
            print('Heap Overflow')
            return
 
        # set data in the allocated node
        node.data = x
 
        # set the .next pointer of the new node to point to the current
        # top node of the list
        node.next = self.top
 
        # update top pointer
        self.top = node
 
        # increase stack's size by 1
        self.nodesCount += 1
 
    # Utility function to check if the stack is empty or not
    def isEmpty(self):
        return self.top is None
 
    # Utility function to return the top element of the stack
    def peek(self):
        # check for an empty stack
        if not self.isEmpty():
            return self.top.data
        else:
            print('The stack is empty')
            exit(-1)
 
    # Utility function to pop a top element from the stack
    def pop(self):            # remove at the beginning
 
        # check for stack underflow
        if self.top is None:
            print('Stack Underflow')
            exit(-1)
 
        # take note of the top node's data
        top = self.top.data
 
        # update the top pointer to point to the next node
        self.top = self.top.next
 
        # decrease stack's size by 1
        self.nodesCount -= 1
 
        return top
 
    # Function to return the size of the stack
    def size(self):
        return self.nodesCount
 
 
if __name__ == '__main__':
 
    stack = Stack()
 
    stack.push(1)
    stack.push(2)
    stack.push(3)
 
    print('Top element is', stack.peek())
 
    stack.pop()
    stack.pop()
    stack.pop()
 
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')
