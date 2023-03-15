from object import Stack


def parentheses_checker(expression: str):
    stack = Stack()
    for element in expression:
        if element == "(":
            stack.push(element)
        elif element == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return True if stack.is_empty() else False


if __name__ == "__main__":
    print(parentheses_checker(""))
    print(parentheses_checker("()()()(())"))
    print(parentheses_checker("())"))
    print(parentheses_checker("(()"))
