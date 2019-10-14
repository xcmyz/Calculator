def get_output(input: str):
    print(input)

    expression = list()
    postfix_expression = list()
    operation_stack = list()

    num_str = ""
    for index, char in enumerate(input):
        if char.isdigit() or char == "." or(index == 0 and (not char.isdigit())):
            num_str += char
        else:
            if num_str != "":
                expression.append(float(num_str))
                num_str = ""
            expression.append(char)
        if index == len(input)-1 and num_str != "":
            expression.append(float(num_str))

    print(expression)

    for z in expression:
        if z not in ['×', '*', '/', '+', '-', '(', ')']:
            postfix_expression.append(z)
        else:
            if z != ')' and (not operation_stack
                             or z == '('
                             or operation_stack[-1] == '('
                             or priority(z) > priority(operation_stack[-1])):
                operation_stack.append(z)
            elif z == ')':
                while True:
                    x = operation_stack.pop()
                    if x != '(':
                        postfix_expression.append(x)
                    else:
                        break
            else:
                while True:
                    if operation_stack \
                            and operation_stack[-1] != '('\
                            and priority(z) <= priority(operation_stack[-1]):
                        postfix_expression.append(operation_stack.pop())
                    else:
                        operation_stack.append(z)
                        break
    while operation_stack:
        postfix_expression.append(operation_stack.pop())
    print(postfix_expression)
    result = cal_postfix_expression(postfix_expression)

    return result


def priority(z):
    if z in ['×', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1


def cal_postfix_expression(postfix_expression):
    num_stack = list()

    for z in postfix_expression:
        if z not in ['×', '*', '/', '+', '-']:
            num_stack.append(z)
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            c = str(b) + z + str(a)
            c = eval(c.strip())
            num_stack.append(c)

    return num_stack[0]
