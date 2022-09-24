class Queue:
    def __init__(self):
        self.queue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.lenght = 0
    
    def push(self, element):
        index = 8
        for f in range(9):
            self.queue[index + 1] = self.queue[index]
            index -= 1
        self.queue[0] = element
        self.lenght += 1

    def delete(self):
        for d in range(self.lenght, 1, -1):
            self.queue[d] = self.queue[d - 1]
        self.lenght -= 1

    def _len(self):
        return self.lenght

s = Queue()

#menu0
while True:
    print("\n1. push element")
    print("2. delete element")
    print("3. lenght queue")
    print("0. quit")
    cmd = input("\nSelect: ")
    print()
    
    if cmd == "1":
        element = float(input("Enter element "))
        s.push(element)

    elif cmd == "2":
        s.delete()

    elif cmd == "3":
        print(s._len())

    elif cmd == "0":
        break

    else:
        print("Wrong command\n")