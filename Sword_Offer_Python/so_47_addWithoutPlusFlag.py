def Add_V1(num1, num2):
    # 这本版本会死循环
    # 因为 python没有无符号右移操作，所以需要越界检查！！！
    res = num1 ^ num2
    carry_flag = (num1 & num2) << 1
    num1 = res
    num2 = carry_flag
    while num2 != 0:
        res = num1 ^ num2
        carry_flag = (num1 & num2) << 1

        num1 = res
        num2 = carry_flag
    return num1

def Add(num1, num2):

    #思路
    # 由于题目要求不能使用四则运算，那么就需要考虑使用位运算
    # 两个数相加可以看成两个数的每个位先相加，但不进位，然后在加上进位的数值
    # 如12+8可以看成1+0=1 2+8=0，由于2+8有进位，所以结果就是10+10=20
    # 二进制中可以表示为1000+1100 先每个位置相加不进位，
    # 则0+0=0 0+1=1 1+0=1 1+1=0这个就是按位异或运算
    # 对于1+1出现进位，我们可以使用按位与运算然后在将结果左移一位
    # 最后将上面两步的结果相加，相加的时候依然要考虑进位的情况，直到不产生进位
    # 按位与运算：相同位的两个数字都为1，则为1；若有一个不为1，则为0。
    # 按位异或运算：相同位不同则为1，相同则为0。

    # 注意python没有无符号右移操作，所以需要越界检查！！！

    while True:
        res = (num1 ^ num2) & 0xffffffff
        carry_flag = ((num1 & num2) << 1) & 0xffffffff

        num1 = res
        num2 = carry_flag
        if num2 == 0 : break
    if num1 <= 0x7fffffff:
        res = num1
    else:
        res = ~(num1^0xffffffff)
    return res

if __name__ == '__main__':
    print(Add(-2,2))