#  35. Search Insert Position

def searchInsert(nums: list[int], target: int) -> int:
    i = 0
    while i < len(nums) and nums[i] < target:
        i += 1
    return i


def test():
    tests = [
       [[1, 3, 5, 6], 5, 2], [[1, 3, 5, 6], 2, 1], [[1, 3, 5, 6], 7, 4]
    ]
    for i in tests:
        print(searchInsert(i[0], i[1]) == i[2])
