class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(1)
s.push("Two")
s.push(3)
s.peek()
s.pop()
s.peek()
s.isEmpty()
s.pop()
s.pop()
s.isEmpty()
