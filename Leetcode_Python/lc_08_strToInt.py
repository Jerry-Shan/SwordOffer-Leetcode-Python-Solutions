import re

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    match = re.findall('^[\+\-]?\d+', str.lstrip())
    # match = re.findall('^[ ]*[\+\-]?\d+', str)
    print(match)
    if len(match) == 0:
        return 0
    num = match[0]
    res = 0
    signFlag = 1
    if num[0] == "-" or num[0] == "+":
        if num[0] == "-":
            signFlag = -1
        for i in range(1, len(num)):
            res = res * 10 + ord(num[i]) - ord('0')
    else:
        for i in range(0, len(num)):
            res = res * 10 + ord(num[i]) - ord('0')
    res = res * signFlag
    if res < -2 ** 31:
        return -2 ** 31
    if res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    return res

if __name__ == '__main__':
    str = '   -12as34'
    print(myAtoi(str))
    print(2**31-1)