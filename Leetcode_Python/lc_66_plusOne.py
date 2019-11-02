from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_flag = True
        for i in range(len(digits) - 1, 0, -1):
            # 进位操作
            if digits[i] != 9 and carry_flag:
                digits[i] = digits[i] + 1
                carry_flag = False

            if digits[i] == 9 and carry_flag:  # 9 且 进位
                digits[i] = 0
                carry_flag = True
        if digits[0] != 9 and carry_flag:
            digits[0] = digits[0] + 1
            carry_flag = False  # 进位 + 1 后，进位符改成 False

        if digits[0] == 9 and carry_flag:
            digits[0] = 0
            digits.insert(0, 1)

        return digits