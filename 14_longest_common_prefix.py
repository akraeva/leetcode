# 14. Longest Common Prefix


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ''
    for i, char in enumerate(strs[0]):
        for s in strs:
            if not i < len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]


def test():
    tests = [[["flower", "flow", "flight"], "fl"],
             [["dog", "racecar", "car"], ""],
             [["reflower", "flow", "flight"], ""],
             [['a'], 'a']
             ]
    for i in tests:
        print(longestCommonPrefix(i[0]) == i[1])


test()


# кто не читает задание, тот я
def longestCommonSubstr(strs: list[str]) -> str:
    res = ['']
    min_str = min(strs, key=len)
    substr = ''
    for i in list(min_str + ' '):
        if len([True for s in strs if i in list(s)]) == len(strs):
            substr += i
        elif substr:
            res.append(substr)
            substr = ''
    return max(res, key=len)