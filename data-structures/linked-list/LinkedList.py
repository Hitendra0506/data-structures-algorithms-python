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

        return True

    def prepend(self, value):

        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

        return True

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
    
    def pop_first(self):
        
        if self.head is None:
            return None
        
        popped_node = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return popped_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr

    def set_value(self, index, value):
        curr = self.get(index)
        
        if curr is None:
            return False
        
        curr.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = prev.next.next
        temp.next = None
        self.length -= 1

        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



