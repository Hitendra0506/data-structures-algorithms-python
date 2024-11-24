'''
LL: Find Middle Node ( ** Interview Question)

Implement the find_middle_node method for the LinkedList class.
Note: this LinkedList implementation does not have a length member variable.
If the linked list has an even number of nodes, return the first node of the second half of the list.

Keep in mind the following requirements:
    - The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
    - When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
    - The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
    - The method should only traverse the linked list once.  In other words, you can only use one loop.


'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while True:
            if fast is None or fast.next is None:
                return slow
            slow = slow.next
            fast = fast.next.next



