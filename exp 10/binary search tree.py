class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value), True
        inserted = False
        if value < root.data:
            root.left, inserted = self.insert(root.left, value)
        elif value > root.data:
            root.right, inserted = self.insert(root.right, value)
        # equal -> duplicate, not allowed
        return root, inserted

    def search(self, root, value):
        if root is None:
            return False
        if value == root.data:
            return True
        if value < root.data:
            return self.search(root.left, value)
        return self.search(root.right, value)

    def min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, root, value):
        if root is None:
            return None, False
        deleted = False
        if value < root.data:
            root.left, deleted = self.delete(root.left, value)
        elif value > root.data:
            root.right, deleted = self.delete(root.right, value)
        else:
            deleted = True
            # Case 1 & 2: no child / one child
            if root.left is None:
                return root.right, True
            if root.right is None:
                return root.left, True
            # Case 3: two children -> inorder successor
            successor = self.min_value_node(root.right)
            root.data = successor.data
            root.right, _ = self.delete(root.right, successor.data)
        return root, deleted

    def inorder(self, root, result):
        if root is not None:
            self.inorder(root.left, result)
            result.append(root.data)
            self.inorder(root.right, result)


def main():
    tree = BST()
    while True:
        print("\n--- BINARY SEARCH TREE ---")
        print("1. Insertion")
        print("2. Deletion")
        print("3. Search")
        print("4. Display (Inorder)")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            value = int(input("Enter value to insert: "))
            tree.root, ok = tree.insert(tree.root, value)
            print("Element inserted successfully" if ok
                  else "Duplicate element, not inserted")
        elif choice == 2:
            value = int(input("Enter value to delete: "))
            tree.root, ok = tree.delete(tree.root, value)
            print("Element deleted successfully" if ok
                  else "Element not found")
        elif choice == 3:
            value = int(input("Enter value to search: "))
            print("Element found" if tree.search(tree.root, value)
                  else "Element not found")
        elif choice == 4:
            if tree.root is None:
                print("Tree is empty")
            else:
                result = []
                tree.inorder(tree.root, result)
                print("Inorder Traversal:")
                print(*result)
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
