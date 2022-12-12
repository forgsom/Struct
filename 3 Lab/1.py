class Linked_List:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    # def insert(self, element, index):
    #     i = 0
    #     node = self.head
    #     prev_node = self.head

    #     while i < index:
    #         prev_node = node
    #         node = node.next_node
    #         i += 1

    #     prev_node.next_node = self.Node(element, next_node=node)

    #     return element

    # def get(self, index):
    #     i = 0
    #     node = self.head
    #     prev_node = self.head

    #     while i < index:
    #         prev_node = node
    #         node = node.next_node
    #         i += 1

    #     prev_node.next_node = self.Node(element, next_node=node)

    #     return node.element

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element
        del node
        return element

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    # def get_lenght(self):
    #     if not self.head:
    #         return 0

    #     i = 1
    #     node = self.head

    #     while node.next_node:
    #         i += 1
    #         node = node.next_node

    #     return i

    def search(self, element):
        node = self.head
        flag = False

        while node.next_node:
            if element in node.element:
                flag = True
            node = node.next_node
        if flag:
            print("the element was found")
        else:
            print("the element is missing")


linked_list = Linked_List()
linked_list.append("Иванов Иван Иванович 1.1.2001")
linked_list.append("Петров Пётр Петрович 2.2.2002")


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
        linked_list.append(element)

    elif cmd == "2":
        index = int(input("Enter index: "))
        linked_list.delete(index)

    elif cmd == "3":
        linked_list.out()

    elif cmd == "4":
        element = input("Enter element: ")
        linked_list.search(element)

    elif cmd == "0":
        break
    else:
        print("Wrong command\n")
