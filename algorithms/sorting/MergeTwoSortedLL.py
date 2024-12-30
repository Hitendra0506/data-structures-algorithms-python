class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, l2):
        dummy = Node(0)
        current = dummy
        i = self.head
        j = l2.head
        while i and j:
            if i.value < j.value:
                current.next = i
                i = i.next
            else:
                current.next = j
                j = j.next
            current = current.next
        if i:
            current.next = i
        if j:
            current.next = j
            self.tail = l2.tail
        
        self.head = dummy.next
        del dummy
        self.length += l2.length
        
            
        
        
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""