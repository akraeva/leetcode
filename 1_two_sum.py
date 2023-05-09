# 1. Two Sum

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)-1, 0, -1):
        j = target - nums[i]
        if j in nums and nums.index(j) != i:
            return [nums.index(j), i]


def test():
    tests = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]],

        ]
    for i in tests:
        print(twoSum(i[0], i[1]) == i[2])


test()
