from typing import List

def twoSum_v1(nums: List[int], target: int) -> List[int]:
    # hashTable{num : index}
    dct = {}
    for index, num in enumerate(nums):
        if target - num in dct:
            return [dct[target - num], index]
        dct[num] = index