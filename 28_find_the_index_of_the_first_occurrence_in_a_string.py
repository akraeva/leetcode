# 28. Find the Index of the First Occurrence in a String

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def test():
    tests = [["sadbutsad", "sad", 0], ["leetcode", "leeto", -1]]
    for i in tests:
        print(strStr(i[0], i[1]) == i[2])
