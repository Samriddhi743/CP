class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []      
        self.increments = []  

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        inc = self.increments[idx]
        if idx > 0:
            self.increments[idx - 1] += inc
        val = self.stack.pop() + inc
        self.increments.pop()
        return val

    def increment(self, k: int, val: int) -> None:
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.increments[idx] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)