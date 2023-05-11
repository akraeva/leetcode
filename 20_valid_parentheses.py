# 20. Valid Parentheses

def isValid(s: str) -> bool:
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for br in s:
        if br in brackets.keys():
            stack.append(br)
        elif br in brackets.values():
            if stack and br == brackets[stack[-1]]:
                stack.pop(-1)
            else:
                return False
    return not stack


def test():
    tests = [["()", True], ['()[]{}', True], ["(]", False]]
    for i in tests:
        print(isValid(i[0]) == i[1])
