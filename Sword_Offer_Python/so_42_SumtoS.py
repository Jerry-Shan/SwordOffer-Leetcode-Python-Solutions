# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

def FindNumbersWithSum(array, tsum):
    # write code here
    my_sum = 0
    start_index = 0
    end_index = len(array) - 1
    while (my_sum != tsum and start_index < end_index):
        my_sum = array[start_index] + array[end_index]
        if my_sum > tsum:
            end_index -= 1
        elif my_sum < tsum:
            start_index += 1
        else:
            return [array[start_index], array[end_index]]
    return []

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8]
    sum = 6
    print(FindNumbersWithSum(array,sum))
