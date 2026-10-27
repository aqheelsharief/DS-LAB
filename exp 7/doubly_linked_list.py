
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

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
        new_node.prev = temp

    def delete_begin(self):
        if self.head is None:
            print("Empty list")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("Empty list")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                print("Element found")
                return
            temp = temp.next

        print("Element not found")

    def display_forward(self):
        if self.head is None:
            print("Empty list")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def display_backward(self):
        if self.head is None:
            print("Empty list")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dll = DLL()

dll.insert_begin(20)
dll.insert_begin(10)
dll.insert_end(30)
dll.insert_end(40)

dll.display_forward()
dll.display_backward()

dll.delete_begin()
dll.delete_end()

dll.display_forward()

dll.search(30)
