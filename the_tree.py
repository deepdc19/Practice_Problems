from collections import deque

class TreeNode():
    '''
    TreeNode represents the binary tree node

    '''
    def __init__(self, value=None):
        self.value = value
        self.left = None  
        self.right = None

class Binarytree():
    '''
    Represent Binary tree and methods on it.

    '''
    def __init__(self, root = None):
        self.root = None
    
    def iterative_in_order_LNR(self):
        final_order = []
        current = self.root
        temp_order = []
        while temp_order or current:
            if current:
                print("current", current)
                temp_order.append(current)
                current = current.left
            else:
                current = temp_order.pop()
                final_order.append(current)
                current = current.right 
        return final_order






