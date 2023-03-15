from object import Stack


def infix_to_postfix(expression: str):
    precedence = {"*": 3,
                  "/": 3,
                  "+": 2,
                  "-": 2,
                  "(": 1}
    stack = Stack()
    postfix = list()
    elements = expression.split()
    for element in elements:
        if element in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfix.append(element)
        elif element == "(":
            stack.push(element)
        elif element == ")":
            top_element = stack.pop()
            while top_element != "(":
                postfix.append(top_element)
                top_element = stack.pop()
        else:
            while not stack.is_empty() and precedence[stack.peek()] >= precedence[element]:
                postfix.append(stack.pop())
            stack.push(element)
    while not stack.is_empty():
        postfix.append(stack.pop())
    return " ".join(postfix)


if __name__ == "__main__":
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

