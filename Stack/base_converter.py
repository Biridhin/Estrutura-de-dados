from object import Stack


def base_converter(decimal: int, base: int):
    stack = Stack()
    digits = "0123456789ABCDEF"
    while decimal > 0:
        stack.push(decimal % base)
        decimal = decimal // base

    s = ""
    while not stack.is_empty():
        s = s + digits[stack.pop()]

    return s


if __name__ == "__main__":
    for c in range(100):
        p = base_converter(c, 2)
        print(p)
    for c in range(100):
        p = base_converter(c, 8)
        print(p)
    for c in range(100):
        p = base_converter(c, 16)
        print(p)
