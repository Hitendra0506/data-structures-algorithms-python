class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            return None
        node_to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = node_to_pop.prev
            self.tail.next = None
            node_to_pop.prev = None
        self.length -= 1
        return node_to_pop
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        node_to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node_to_pop.next
            node_to_pop.next = None
            self.head.prev = None
        self.length -= 1
        return node_to_pop
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index <= self.length // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length - 1, index, -1):
                curr = curr.prev
        return curr
    
    def set_value(self, index, value):
        node_to_set = self.get(index)
        if node_to_set is None:
            return False
        node_to_set.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        before = self.get(index - 1)
        after = before.next
        new_node = Node(value)
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        node_to_remove = self.get(index)
        before = node_to_remove.prev
        after = node_to_remove.next
        node_to_remove.next = None
        node_to_remove.prev = None
        before.next = after
        after.prev = before
        self.length -= 1
        return node_to_remove
