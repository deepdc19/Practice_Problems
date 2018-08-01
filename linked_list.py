class node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None 
class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        temp = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = temp
    
    def length(self):
        current = self.head
        size = 0
        while current.next != None:
            size += 1
            current = current.next 
        return size 

    def display(self):
        temp = []
        current = self.head 
        while current.next != None:
            current = current.next
            temp.append(current.data)
        print (temp)
    
    def getIndex(self,index):
        if index >= self.length():
            return "The index is out of range"
        temp = self.head.next
        pos = 0
        while pos != index:
            temp = temp.next 
            pos += 1
        return temp.data
    
    def getMiddle(self):
        if self.length() % 2 == 0: 
            middle = self.getIndex(self.length() / 2)
            return middle
        return self.getIndex(((self.length() + 1) / 2) - 1)  
        
        
        



