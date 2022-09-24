class Stack:
    def __init__(self):
        self.stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.lenght = len(self.stack)
    
    def push(self, element):
        index = 8
        for f in range(9):
            self.stack[index + 1] = self.stack[index]
            index -= 1
        self.stack[0] = element

        #self.stack.append(element)

    def pop(self):
        for d in range(1, 9):
            self.stack[d - 1] = self.stack[d]
        #self.stack.pop(self.lenght - 1)

    def top(self):
        return self.stack[0]
        #return self.stack[self.lenght - 1]

s = Stack()

#menu
while True:
    print("\n1. push element")
    print("2. pop element")
    print("3. top element")
    print("0. quit")
    cmd = input("\nSelect: ")
    print()
    
    if cmd == "1":
        element = float(input("Enter element "))
        s.push(element)

    elif cmd == "2":
        s.pop()

    elif cmd == "3":
        print(s.top())

    elif cmd == "0":
        break

    else:
        print("Wrong command\n")