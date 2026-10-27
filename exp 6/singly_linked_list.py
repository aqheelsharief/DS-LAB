
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("Empty list")
            return

        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Empty list")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                print("Element found")
                return
            temp = temp.next

        print("Element not found")

    def display(self):
        if self.head is None:
            print("Empty list")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SLL()

sll.insert_begin(20)
sll.insert_begin(10)
sll.insert_end(30)
sll.insert_end(40)

sll.display()

sll.delete_begin()
sll.delete_end()

sll.display()

sll.search(30)
