class Queue:
    def __init__(self):
        self.items: list = []
        self.size: int = 0

    def __repr__(self):
        return f"Queue(size: {self.size}, items: {self.items})"

    def __len__(self):
        return self.size

    def enqueue(self, item) -> None:
        self.items.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            first = self.items[0]
            del self.items[0]
            return first
        raise "The queue is empty!"

    def is_empty(self) -> bool:
        return self.items == []


if __name__ == "__main__":
    q = Queue()
    q.enqueue(2)
    q.enqueue("pipoca")
    print(q)
    print(len(q))
