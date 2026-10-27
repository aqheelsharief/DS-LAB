
class stack:
    def __init__(self, n):
        self.size = n
        self.stack = [None] * self.size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, ele):
        if self.isFull():
            print('Stack overflow')
            return
        self.top += 1
        self.stack[self.top] = ele

    def pop(self):
        if self.isEmpty():
            print('Stack underflow')
            return -1
        item, self.top = self.stack[self.top], self.top - 1
        return item

    def peek(self):
        if self.isEmpty():
            print('Stack underflow')
            return None
        return self.stack[self.top]

    def display(self):
        if self.isEmpty():
            print("Empty stack")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])


def evaluate_postfix(expression):
    Stack = stack(len(expression))

    for ch in expression:
        if ch.isspace():
            continue

        if ch.isdigit():
            Stack.push(int(ch))

        else:
            b = Stack.pop()
            a = Stack.pop()

            if ch == '+':
                Stack.push(a + b)
            elif ch == '-':
                Stack.push(a - b)
            elif ch == '*':
                Stack.push(a * b)
            elif ch == '/':
                Stack.push(a / b)
            elif ch == '^':
                Stack.push(a ** b)

    return Stack.pop()


expression = input("Enter postfix expression: ")
result = evaluate_postfix(expression)
print("Result:", result)
