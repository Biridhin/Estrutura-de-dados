from object import Stack


def postfix_calculator(expression: str) -> float:
    do_math = {"*": lambda op1, op2: op1 * op2,
               "/": lambda op1, op2: op1 / op2,
               "+": lambda op1, op2: op1 + op2,
               "-": lambda op1, op2: op1 - op2}
    operands = Stack()
    elements = expression.split()
    for element in elements:
        if element in "0123456789":
            operands.push(int(element))
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            result = do_math[element](op1, op2)
            operands.push(result)
    return operands.pop()


if __name__ == "__main__":
    print(postfix_calculator('7 8 + 3 2 + /'))

