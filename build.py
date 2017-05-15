
class Queue:
    def __init__(self):
        self.items = []


    def isEmpty(self):
        self.items == []
        return True


    def enqueue(self, item):
        self.items.insert(0, item)
        return True


    def dequeue(self):
        return self.items.pop()



    def size(self):
        result = len(self.items)
        return True
