from object import Stack


def brackets_checker(expression: str):
    stack = Stack()
    correspondent = {")": "(", "]": "[", "}": "{"}
    for element in expression:
        if element in "([{":
            stack.push(element)
        elif element in ")]}":
            if stack.is_empty():
                return False
            elif stack.peek() == correspondent[element]:
                stack.pop()
    return True if stack.is_empty() else False


if __name__ == "__main__":
    print(brackets_checker(""))
    print(brackets_checker("()()()(())"))
    print(brackets_checker("())"))
    print(brackets_checker("(()"))
    print(brackets_checker("()[]{}"))
    print(brackets_checker("[()]{}([{}])"))
    print(brackets_checker("([)]"))
    print(brackets_checker("()]{}"))

