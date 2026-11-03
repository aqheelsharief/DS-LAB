class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack Underflow")
            return
        print("Stack elements:")
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next


def main():
    stack = Stack()
    while True:
        print("\n--- STACK USING LINKED LIST ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to push: ")
            stack.push(item)
            print("Item pushed successfully")
        elif choice == "2":
            item = stack.pop()
            if item is not None:
                print("Popped item is", item)
        elif choice == "3":
            item = stack.peek()
            if item is not None:
                print("Top item is", item)
        elif choice == "4":
            stack.display()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
