# Stack

Stack is a data structure to store data in FILO (First-In Last-Out) format. For an example if you browse a website, browser will store your history and if you want to go back one page browser will know which page is your previous.

![Example](/stack/resource/browsing_example.png)

## How To Create It

### Create Your Stack Class

In this class it will have maximum data in the stack. If you dont want any limit data you can provide it '-1' value.

```python
class Stack():
    # Constructor
    def __init__(self, data, size: int):
        self.stack = []
        self.max_stack = -1

        if size is not None and size > 0:
            self.max_stack = size

        if data is not None:
            self.stack.append(data)
```

### Fullness Check Method

Implement our first method is checking if the stack is full by comparing `number of the data` to `maximum`.

```python
def is_full(self):
    return len(self.stack) == self.max_stack
```

### Emptiness Check Method

Implement another checking method if the stack is empty by comparing `number of the data` to 0.

```python
def is_empty(self):
    return len(self.stack) == 0
```

### Push Method

In the push method we will check if the stack is full or not before append new data into our stack. In this method we'll push new data into the top of the stack and return `None`.

```python
def push(self, data):
    if not self.is_full():
        self.stack.append(data)
```

### Pop Method

In the pop method we will check if the stack is empty because we don't want to remove data from empty stack. In this method we'll get the top data and remove it from the stack.

```python
def pop(self):
    if self.is_empty():
        return ""

    data = self.stack.pop()
    return data
```

### Peak Method

In the peak method is the same as pop but it does not remove data from stack.

```python
def peek(self):
    if self.is_empty():
        return ""

    data = self.stack.pop()
    self.stack.append(data)
    return data
```

### Testing

```python
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
```
