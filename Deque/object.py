class Deque:
    def __init__(self):
        self.items: list = []
        self.size: int = 0

    def __repr__(self):
        return f"Deque(size: {self.size}, items: {self.items})"

    def __len__(self):
        return self.size

    def add_front(self, item) -> None:
        self.items.append(item)
        self.size += 1

    def add_rear(self, item) -> None:
        self.items.insert(0, item)
        self.size += 1

    def remove_front(self):
        self.size -= 1
        return self.items.pop()

    def remove_rear(self):
        self.size -= 1
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return self.items == []
