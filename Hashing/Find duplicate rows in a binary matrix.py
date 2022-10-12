# A class to store a Trie node
class Trie:
    # Constructor
    def __init__(self):
        self.character = [None] * 2
 
        # set when the node is a leaf node
        self.isLeaf = False
 
 
# Iterative function to insert each element of a list into a Trie
def insert(head, A):
 
    # start from the root node
    curr = head
 
    for i in A:
        # create a new node if the path doesn't exist
        if curr.character[i] is None:
            curr.character[i] = Trie()
 
        # go to the next node
        curr = curr.character[i]
 
    # if the row is inserted before, return false
    if curr.isLeaf:
        return False
 
    # mark leaf node and return true
    curr.isLeaf = True
    return True
 
 
if __name__ == '__main__':
 
    mat = [
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0]
    ]
 
    # insert all rows of the matrix into a Trie
    head = Trie()
    for i, e in enumerate(mat):
        if not insert(head, e):
            print(f"Duplicate row found: Row #{i+1}")
 
