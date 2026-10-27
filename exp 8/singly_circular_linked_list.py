
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SCLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def delete_begin(self):
        if self.head is None:
            print("Empty list")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

    def delete_end(self):
        if self.head is None:
            print("Empty list")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    def search(self, key):
        if self.head is None:
            print("Empty list")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print("Element found")
                return

            temp = temp.next

            if temp == self.head:
                break

        print("Element not found")

    def display(self):
        if self.head is None:
            print("Empty list")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(head)")


scll = SCLL()

scll.insert_begin(20)
scll.insert_begin(10)
scll.insert_end(30)
scll.insert_end(40)

scll.display()

scll.delete_begin()
scll.delete_end()

scll.display()

scll.search(30)
