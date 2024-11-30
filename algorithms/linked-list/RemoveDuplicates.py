'''
LL: Remove Duplicates ( ** Interview Question)
You are given a singly linked list that contains integer values, where some of these values may be duplicated.

Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
You can implement the remove_duplicates() method in two different ways:

Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.
Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.

Here is the method signature you need to implement: def remove_duplicates(self):


Example:

Input:
LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5

Output:
LinkedList: 1 -> 2 -> 3 -> 4 -> 5
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))
    
    def remove_duplicates(self):
        seen = set()
        curr = self.head
        prev = None
        while curr:
            if curr.value in seen:
                prev.next = curr.next
                self.length -= 1
            else:
                seen.add(curr.value)
                prev = curr
            curr = curr.next