
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


def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0


def infix_to_postfix(expression):
    Stack = stack(len(expression))
    postfix = ''

    for ch in expression:
        if ch.isspace():
            continue

        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            Stack.push(ch)

        elif ch == ')':
            while not Stack.isEmpty() and Stack.peek() != '(':
                postfix += Stack.pop()

            if not Stack.isEmpty():
                Stack.pop()  # Remove '('

        else:
            while (not Stack.isEmpty()
                   and Stack.peek() != '('
                   and (precedence(Stack.peek()) > precedence(ch)
                        or (precedence(Stack.peek()) == precedence(ch)
                            and ch != '^'))):
                postfix += Stack.pop()

            Stack.push(ch)

    while not Stack.isEmpty():
        postfix += Stack.pop()

    return postfix


expression = input('Enter infix expression: ')
result = infix_to_postfix(expression)
print('Postfix Expression:', result)
