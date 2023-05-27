class Queue():
    # Constructor
    def __init__(self, data=None, size=-1):
        self.queue = []
        self.max_queue = -1

        if size is not None and size > 0:
            self.max_queue = size

        if data is not None:
            self.queue.append(data)

    def is_full(self):
        return len(self.queue) == self.max_queue

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        if not self.is_full():
            self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return ""

        data = self.queue[0]
        self.queue.remove(data)
        return data

    def peek(self):
        if self.is_empty():
            return ""

        data = self.queue.pop()
        self.queue.append(data)
        return data


def main():
    queue = Queue(1)
    queue.enqueue(2)
    print(f"Customer id : {queue.peek()} enter the queue")
    print(f"Serving for customer id : {queue.dequeue()}")
    print(f"Who is the next customer id? Ans: id : {queue.peek()}")


if __name__ == "__main__":
    main()
