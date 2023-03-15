class Stack:
    def __init__(self):
        self.items: list = []
        self.size: int = 0

    def __repr__(self):
        return f"Stack(size: {self.size}, items: {self.items})"

    def __len__(self):
        return self.size

    def push(self, item: int = 2) -> None:
        self.items.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self) -> bool:
        return self.items == []


if __name__ == "__main__":
    pilha_1 = Stack()
    pilha_2 = Stack()

    pilha_1.push(3)
    pilha_1.is_empty()

    print(pilha_1)

