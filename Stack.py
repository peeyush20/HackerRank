class Stack:
    def __init__(self):
        self.s = []

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            return self.s[-1]
        else:
            print('Stack is empty, nothing to return!')

    def push(self,element):
        self.s.append(element)
        print('Added ' + str(element) + ' to top of the stack')
        print('Stack Content: ',end='')
        self.print_content()

    def pop(self):
        if not self.isEmpty():
            copy = self.s[-1]
            del self.s[-1]
            print('Removed '+str(copy) + ' from top of the stack')
            print('Stack Content: ', end='')
            self.print_content()
            return copy
        else:
            print('Oops! Stack is empty! Nothing to pop!')

    def print_content(self):
        print(self.s)

s = Stack()
s.push(5)
s.push(10)
s.push(20)
e = s.pop()
e = s.pop()
s.push(3)

s.print_content()