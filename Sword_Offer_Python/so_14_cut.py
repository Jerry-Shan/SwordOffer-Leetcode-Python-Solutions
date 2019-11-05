def cutRope_v2(number):
    # write code here
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    times_of_three = number // 3
    if number % 3 == 1:
        times_of_three -= 1
    times_of_two = (number - (3 * times_of_three)) // 2

    return (3 ** times_of_three) * (2 ** times_of_two)

def cutRope_v1(number):
    # write code here
    if number <= 1:
        return 0
    if number == 2:
        return 1
    if number == 3:
        return 2
    dp = [-1] * (number + 1)
    dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
    max_area = 0
    for i in range(4, number + 1):
        for j in range(1, (i // 2) + 1):
            temp = dp[j] * dp[i-j]
            if temp > max_area:
                max_area = temp
        dp[i] = max_area
    return max_area


if __name__ == '__main__':
    print(cutRope_v1(10))