class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def peek(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        print("Queue elements:")
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next


def main():
    queue = Queue()
    while True:
        print("\n--- QUEUE USING LINKED LIST ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            print("Item enqueued successfully")
        elif choice == "2":
            item = queue.dequeue()
            if item is not None:
                print("Dequeued item is", item)
        elif choice == "3":
            item = queue.peek()
            if item is not None:
                print("Front item is", item)
        elif choice == "4":
            queue.display()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
