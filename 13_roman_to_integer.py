# 13. Roman to Integer


def romanToInt(s: str) -> int:
    abc = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    nums = [abc[i] for i in list(s)]
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1]:
            nums[i] *= -1
    return sum(nums)


def test():
    tests = [["III", 3], ["LVIII", 58], ["MCMXCIV", 1994]]
    for i in tests:
        print(romanToInt(i[0]) == i[1])
