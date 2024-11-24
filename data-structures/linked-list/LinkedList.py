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

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):

        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def print_list(self):

        curr = self.head

        while curr is not None:
            print(curr.value)
            curr = curr.next

    def make_empty(self):
        
        self.head = None
        self.tail = None
        self.length = 0
