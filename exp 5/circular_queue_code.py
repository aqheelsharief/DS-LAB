class CQ:
    def __init__(self, size):
        self.q = [None]*size
        self.size = size
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.front == (self.rear + 1) % self.size 

    def enqueue(self, ele):
        if self.isFull():
            print("Overflow")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = ele
        print("item inserted")
        return
    
    def dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        ele = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1) % self.size
        print("item deleted")
        return ele

    def peek(self):
        if self.isEmpty():
            print("Empty")
            return
        print(self.q[self.front])

    def display(self):
        if self.isEmpty():
            print("Empty")
            return
        p = self.front
        while p == self.rear:
            print(self.q[p])
            p = (p+1) % self.size
        print(self.q[p])
