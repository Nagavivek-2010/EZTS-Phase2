class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("LinkedList is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def delete_beginning(self):
        if self.head is None:
            print("LinkedList is empty.")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("LinkedList is empty.")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("LinkedList is empty.")
        else:
            if position == 0:
                self.head = self.head.next
            else:
                current = self.head
                for _ in range(position - 1):
                    current = current.next
                    if current is None:
                        print("Invalid position.")
                        return
                if current.next is None:
                    print("Invalid position.")
                else:
                    current.next = current.next.next


# Example usage:
my_list = LinkedList()

my_list.append(5)
my_list.append(10)
my_list.append(15)
my_list.append(20)
my_list.append(25)

my_list.display()  # Output: 5 -> 10 -> 15 -> 20 -> 25 -> None

my_list.delete_beginning()
my_list.display()  # Output: 10 -> 15 -> 20 -> 25 -> None

my_list.delete_end()
my_list.display()  # Output: 10 -> 15 -> 20 -> None

my_list.delete_at_position(1)
my_list.display()  # Output: 10 -> 20 -> None
