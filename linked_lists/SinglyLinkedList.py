class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
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

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        previous_node = self.head
        current_node = self.head.next

        while current_node is not None:
            if current_node.data == data:
                previous_node.next = current_node.next
                return

            previous_node = current_node
            current_node = current_node.next

    def __str__(self):
        if not self.head:
            return "List is empty"

        output = ""

        curr = self.head
        while curr:
            output += str(curr.data) + "->"
            curr = curr.next
        output = output[:-2]

        return output.strip()


def singly_linked_list_example():
    sll = SinglyLinkedList()

    # Insert Data
    sll.insert_at_beginning("Hello")
    sll.insert_at_beginning("World")

    sll.insert_at_end("World")

    # Print Linked List
    print(sll)  # World->Hello->World

    # Remove Data
    sll.delete("World")

    # Print Linked List
    print(sll)  # Hello->World


if __name__ == "__main__":
    singly_linked_list_example()
