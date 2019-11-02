from typing import List


class Solution:
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        # a + b + c == 0, find a,b,c
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] > nums[i - 1]:  # 去重
                left, right = i + 1, len(nums) - 1
                if nums[i] + nums[left] + nums[left + 1] > 0 or nums[i] + nums[right - 1] + nums[right] < 0:
                    continue
                while left < right:
                    sumThree = nums[i] + nums[left] + nums[right]
                    if sumThree == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 去重
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sumThree > 0:  # 说明值大了
                        right -= 1
                    else:
                        left += 1
        return res