def solve(N, X, prices):
    # 初始化一维DP数组
    dp = [-1] * (X + 1)
    dp[0] = 0  # 基础情况：不选择任何物品，总价值为0

    for i in range(N):
        # 从后向前更新，避免覆盖还需要使用的数据
        for j in range(X, prices[i] - 1, -1):
            if dp[j - prices[i]] != -1:
                dp[j] = max(dp[j], dp[j - prices[i]] + 1)

    # 找到最大物品数
    max_items = max(dp)

    # 在最大物品数的情况下，找到最大总价值
    max_value = 0
    for j in range(X, -1, -1):
        if dp[j] == max_items:
            max_value = j
            break

    return X - max_value


# 读取输入
N, X = map(int, input().split())
prices = [int(input()) for _ in range(N)]

# 计算并输出结果
result = solve(N, X, prices)
print(result)