class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            prev, curr_min = self.stack[-1]
            self.stack.append((val, min(curr_min, val)))

    def pop(self) -> None:
        self.stack.pop() 

    def top(self) -> int:
        num, m = self.stack[-1]
        return num

    def getMin(self) -> int:
        num, m = self.stack[-1]
        return m
        
