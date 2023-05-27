# Queue

Queue is a data structure to store data in FIFO (First-In First-Out) format. Let's imagine about ticketing system for a movie theater. The system needs to handle the queue of customers waiting to purchase tickets. As customers arrive, they join the end of the queue. When a cashier becomes available, they serve the customer at the front of the queue and remove them from the system.

![Example](/queue/resource/buy_ticket_example.png)

## How To Create It

### Create Your Queue Class

In this class it will have maximum data in the queue. If you dont want any limit data you can provide it '-1' value.

```python
class Queue():
    # Constructor
    def __init__(self, data=None, size=-1):
        self.queue = []
        self.max_queue = -1

        if size is not None and size > 0:
            self.max_queue = size

        if data is not None:
            self.queue.append(data)
```

### Fullness Check Method

Implement our first method is checking if the queue is full by comparing `number of data` to `maximum` number we provide.

```python
def is_full(self):
    return len(self.queue) == self.max_queue
```

### Emptiness Check Method

Implement another checking method if the queue is empty by comparing `number of data` to 0.

```python
def is_empty(self):
    return len(self.queue) == 0
```

### Enqueue Method

In the push method we will check if the queue is full or not before adding new data into our queue. In this method we'll push new data into the queue and return `None`.

```python
def enqueue(self, data):
    if not self.is_full():
        self.queue.append(data)
```

### Dequeue Method

In the pop method we will check if the queue is empty because we don't want to remove data from empty queue. In this method we'll get the front data and remove it from the queue.

```python
def dequeue(self):
    if self.is_empty():
        return ""

    data = self.queue[0]
    self.queue.remove(data)
    return data
```

### Peak Method

In the peak method is the same as dequeue but it does not have to remove data from queue and it'll return the front data.

```python
def peek(self):
    if self.is_empty():
        return ""

    data = self.queue.pop()
    self.queue.append(data)
    return data
```

### Testing

```python
def main():
    queue = Queue(1)
    queue.enqueue(2)
    print(f"Customer id : {queue.peek()} enter the queue")
    print(f"Serving for customer id : {queue.dequeue()}")
    print(f"Who is the next customer id? Ans: id : {queue.peek()}")

if __name__ == "__main__":
    main()
```
