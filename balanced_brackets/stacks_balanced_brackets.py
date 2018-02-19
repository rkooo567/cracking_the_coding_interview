class Stack(object):
    def __init__(self):
        self.data = []
    
    def push(self, item):
        self.data.append(item)
        
    def pop(self):
        return self.data.pop()
        
    def top(self):
        """ Don't forget to handle the error when there's no data """
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]
        
    def empty(self):
        return len(self.data) == 0
        
def is_matched(brackets):
    bracket_matches = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    check_matches = Stack()
    for bracket in brackets:
        if bracket in bracket_matches.keys():
            if check_matches.top() == bracket_matches[bracket]:
                check_matches.pop()
            else:
                return False
        else:
            check_matches.push(bracket)
    if check_matches.empty():
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")