class Node:

    def __init__(self, value):
        
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def prepend(self, value):

        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    def print_list(self):
        vals = []

        curr = self.head
        while curr is not None:
            vals.append(curr.value)
            curr = curr.next
        
        print(' -> '.join(vals))

    def make_empty(self):
        
        self.head = None
        self.tail = None
        self.length = 0

    def pop(self):
        if self.tail is None:
            return None
            
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        
        popped_node = self.tail
        curr.next = None
        self.tail = curr
        
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        
        return popped_node

