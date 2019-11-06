# 题目描述：
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False

# 思路1： 暴力法
def duplicate_v1(numbers, duplication):
    # write code here
    if not numbers or len(numbers) <=1:
        return False
    help_nums = []
    for num in numbers:
        if num not in help_nums:
            help_nums.append(num)
        else:
            duplication[0] = num
            print(num)
            return True
    return False

# 思路2：排序法，和前一个一样则证明重复了
def duplicate_v2(numbers, duplication):
    # write code here
    if not numbers or len(numbers) <=1:
        return False
    numbers_sorted = sorted(numbers)
    for i in range(1,len(numbers_sorted)):
        if numbers_sorted[i] == numbers_sorted[i-1]:
            return True
    return False

if __name__ == '__main__':
    nums = [1,2,3,4,2,3,5,6]
    duplication = [0]*2
    print(duplicate_v2(nums,duplication))