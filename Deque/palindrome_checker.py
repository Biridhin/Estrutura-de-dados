from object import Deque


def palindrome_checker(string: str) -> bool:
    deque = Deque()

    for c in string:
        deque.add_front(c)

    while len(deque) > 1:
        first = deque.remove_front()
        second = deque.remove_rear()
        if first != second:
            return False
    return True


if __name__ == "__main__":
    print(palindrome_checker("radar"))
    print(palindrome_checker("abccba"))
    print(palindrome_checker("pipoca"))
    print(palindrome_checker("lambda"))
