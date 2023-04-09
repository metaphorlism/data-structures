class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        current_node = self.head.next

        while current_node is not None:
            if current_node.data == data:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return

            current_node = current_node.next

    def __str__(self):
        if not self.head:
            return "List is empty"

        output = ""

        curr = self.head
        while curr:
            output += str(curr.data) + "<->"
            curr = curr.next
        output = output[:-3]

        return output.strip()


def doubly_linked_list_example():
    dll = DoublyLinkedList()

    # Insert Data
    dll.insert_at_beginning("Hello")
    dll.insert_at_beginning("World")

    dll.insert_at_end("World")

    # Print Linked List
    print(dll)  # World->Hello->World

    # Remove Data
    dll.delete("World")

    # Print Linked List
    print(dll)  # Hello->World


if __name__ == "__main__":
    doubly_linked_list_example()
