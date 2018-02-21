class Stack(object):
    def __init__(self):
        self.data = []
        self.size = 0
    
    def push(self, value):
        self.data.append(value)
        self.size += 1
    
    def pop(self):
        last_index = len(self.data) - 1
        self.size -= 1
        return self.data.pop(last_index)
    
    def peek(self):
        return self.data[-1]
    
    def is_empty(self):
        return self.size == 0
    
class MyQueue(object):
    def __init__(self):
        self.enque_stack = Stack()
        self.deque_stack = Stack()
    
    def peek(self):
        if self.deque_stack.is_empty():
            move_stack(self.enque_stack, self.deque_stack)
        return self.deque_stack.peek()
    
    def pop(self):
        if self.deque_stack.is_empty():
            move_stack(self.enque_stack, self.deque_stack)
        last_value = self.deque_stack.pop()
        return last_value
            
    def put(self, value):
        self.enque_stack.push(value)
        
def move_stack(a, b):
    """
        move all the data in one stack (a) to another stack (b)
    """
    while not a.is_empty():
        last_value = a.pop()
        b.push(last_value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        