class Double_List:
    class Node:
        previous_node = None
        next_node = None
        element = None

        def __init__(self, element, next_node=None, previous_node=None) -> None:
            self.element = element
            self.next_node = next_node
            self.previous_node = previous_node

    head = None
    tail = None
    lenght = 0

    def append(self, element):
        self.lenght += 1
        if not self.head:
            self.head = self.Node(element)
            return element
        elif not self.tail:
            self.tail = self.Node(element, None, self.head)
            self.head.next_node = self.tail
            return element
        else:
            self.tail = self.Node(element, None, self.tail)
            self.tail.previous_node.next_node = self.tail
            return element

    def _del(self, index, reverse=False):
        if index == 0:
            element = self.head.element
            self.head = self.head.next_node
            self.head.previous_node = None
            return element
        elif index == self.lenght - 1:
            element = self.tail.element
            self.tail = self.tail.previous_node
            self.tail.next_node = None
            return element
        elif reverse:
            i = self.lenght - 1
            node = self.tail

            while i != index:
                node = node.previous_node
                i -= 1

            element = node.element
            node.previous_node.next_node, node.next_node.previous_node = (
                node.next_node,
                node.previous_node,
            )
            del node
            return element
        else:
            i = 0
            node = self.head

            while i != index:
                node = node.next_node
                i += 1

            element = node.element
            node.previous_node.next_node, node.next_node.previous_node = (
                node.next_node,
                node.previous_node,
            )
            del node
            return element

    def delete(self, index):
        if self.head:
            if index > self.lenght // 2:
                element = self._del(index, reverse=True)
            elif index <= self.lenght // 2:
                element = self._del(index, reverse=False)
            self.lenght -= 1
            return element

    def Out(self):
        node = self.head
        while node:
            print(node.element)
            node = node.next_node

    def reverseOut(self):
        node = self.tail
        while node:
            print(node.element)
            node = node.previous_node

    def search(self, element):
        node = self.head
        flag = False

        while node.next_node:
            if element in node.element:
                flag = True
            elif element in self.tail.element:
                flag = True
            node = node.next_node
        if flag:
            print("the element was found")
        else:
            print("the element is missing")

    def __iter__(self):
        node = self.head
        while node:
            yield node.element
            node = node.next_node


if __name__ == "__main__":
    double_list = Double_List()

double_list.append("Нижневартовск 261к")
double_list.append("Сургут 321к")
double_list.append("Когалым 61к")
double_list.append("Лангепас 43к")

# menu
while True:
    print("\n1. append element")
    print("2. delete element")
    print("3. show all element")
    print("4. search element")
    print("0. quit")
    cmd = input("\nSelect: ")
    print()

    if cmd == "1":
        element = input("Enter element: ")
        double_list.append(element)

    elif cmd == "2":
        index = int(input("Enter index: "))
        double_list.delete(index)

    elif cmd == "3":
        print("1. Right element")
        print("2. Reverse element")
        cmd_temp = input("\nSelect: ")
        print()

        if cmd_temp == "1":
            double_list.Out()

        elif cmd_temp == "2":
            double_list.reverseOut()

    elif cmd == "4":
        element = input("Enter element: ")
        double_list.search(element)

    elif cmd == "0":
        break
    else:
        print("Wrong command\n")
