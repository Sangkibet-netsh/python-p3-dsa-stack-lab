class Stack:

    def __init__(self, items=None, max_size=None):
        if items is None:
            items = []
        self.items = items
        self.max_size = max_size

    def push(self, item):
        if self.max_size is not None and len(self.items) >= self.max_size:
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def full(self):
        if self.max_size is None:
            return False
        return self.size() >= self.max_size

    def search(self, item):
        if item not in self.items:
            return -1
        return self.size() - self.items.index(item) - 1