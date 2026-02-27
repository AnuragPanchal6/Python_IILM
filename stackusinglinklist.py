class Node:
    def __init__(self,data = None):
        self.value = data
        self.next = None

class Stack:
    def __int__(self):
        self.top =None
    
    def push(self , data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return 