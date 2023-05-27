class Stack():
    # Constructor
    def __init__(self, data, size: int):
        self.stack = []
        self.max_stack = -1

        if size is not None and size > 0:
            self.max_stack = size

        if data is not None:
            self.stack.append(data)

    def is_full(self):
        return len(self.stack) == self.max_stack

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return ""

        data = self.stack.pop()
        return data

    def peek(self):
        if self.is_empty():
            return ""

        data = self.stack.pop()
        self.stack.append(data)
        return data


def main():
    stack = Stack("https://www.google.com/", -1)
    print("Search Wiki in Google")
    stack.push("https://www.google.com/search?q=wiki")
    print("Add 'https://www.google.com/search?q=wiki' into the stack")
    print("Click on the wiki link")
    stack.push("https://en.wikipedia.org/wiki/Wiki")
    print("Add 'https://en.wikipedia.org/wiki/Wiki' into the stack")
    print("Go back 1 page")
    print(f"Redirect from '{stack.pop()}' to '{stack.peek()}'")


if __name__ == "__main__":
    main()
