# 9. Palindrome Number


def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def test():
    tests = [[121, True], [-121, False], [10, False]]
    for i in tests:
        print(isPalindrome(i[0]) == i[1])


test()
