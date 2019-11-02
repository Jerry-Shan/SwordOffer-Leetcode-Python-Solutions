# date: 2019-10-31

def printMatrix(matrix):
    # write code here
    # 思路： 上下左右四个边界，一次打印一圈,然后边界减小
    if not matrix:
        return
    left = 0
    up = 0
    right = len(matrix[0]) - 1
    down = len(matrix) - 1
    res = []
    while left <= right and up <= down:
        # left -> right
        if left < right:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
        # up -> down
        if up < down:
            for i in range(up+1, down + 1):
                res.append(matrix[i][right])
            # right -= 1
        # right -> left
        if left < right and up != down: # up != down 排除只剩下一行的情况
            for i in range(right-1, left - 1, -1):
                res.append(matrix[down][i])
        # down -> up
        if up < down and left != right: # left != right 排除只有一列的情况
            for i in range(down-1, up, -1):
                res.append(matrix[i][left])
        right -= 1
        down -= 1
        left += 1
        up += 1
    return res


if __name__ == '__main__':
    grid = [[1,6,9],[2,3,4]]
    print(printMatrix(grid))