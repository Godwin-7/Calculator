def tokenize(expression):
    tokens = []
    value = ""
    for char in expression:
        if char.isdigit() or char == '.':
            value += char
        else:
            if value:
                tokens.append(value)
                value = ""
            if char in "+-*/()":
                tokens.append(char)
    if value:
        tokens.append(value)
    return tokens

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token.isnumeric() or '.' in token:
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if token.isnumeric() or '.' in token:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

def calculate(expression):
    tokens = tokenize(expression)
    postfix_tokens = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix_tokens)
    return result

# Example usage:
expression = "3 + 5 * ( 2 - 8 )"
result = calculate(expression)
print(f"The result of the expression '{expression}' is: {result}")