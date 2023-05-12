# 27. Remove Element

def removeElement(nums: list[int], val: int) -> int:
    val_index = [i for i, num in enumerate(nums) if num == val]
    val_index.reverse()
    for i in val_index:
        nums.pop(i)
    k = len(nums)
    return k


def test():
    tests = [[[3, 2, 2, 3], 3, 2, [2, 2]],
             [[0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 4, 0, 3]]]
    for i in tests:
        print(removeElement(i[0], i[1]) == i[2])
