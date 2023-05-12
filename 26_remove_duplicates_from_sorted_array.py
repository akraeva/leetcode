# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums: list[int]) -> int:
    abc = {i: 0 for i in set(nums)}
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        if abc[num] == 0:
            abc[num] = 1
        else:
            nums.pop(i)
    k = len(nums)
    return k


def test():
    tests = [[[1, 1, 2], 2, [1, 2]], 
             [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]]]
    for i in tests:
        print(removeDuplicates(i[0]) == i[1])
