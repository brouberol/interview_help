# Write a function that given a string detects whether all parentheses are 
# matched


def balanced(s):
    stack = []
    for char in s:
        if char not in ['(', ')']:
            continue
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return not stack
