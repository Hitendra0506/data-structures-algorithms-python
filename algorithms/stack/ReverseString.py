'''
Stack: Reverse String ( ** Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.
'''

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def reverse_string(inp):
    stack = Stack()
    for i in inp:
        stack.push(i)
    res = ''
    while not stack.is_empty():
        res += stack.pop()
    return res
