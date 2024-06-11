
# 1. 矩阵动态规划
def count_diet_plans(N, S, T, A, B):
    # N+1(天) * T+1(体重范围0~T)
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    # 第0天体重为S，1代表体重S<=T有1种计划
    dp[0][S] = 1

    for i in range(1, N + 1):
        for j in range(T + 1):
            # 第i-1天体重为j有计划
            if dp[i - 1][j] > 0:
                # 第i-1天减重后>=0
                if j - A[i - 1] >= 0:
                    # 第i天体重为j - A[i - 1]的计划数累加前一天计划数
                    dp[i][j - A[i - 1]] += dp[i - 1][j]
                # 第i-1天增重后<=T
                if j + B[i - 1] <= T:
                    # 第i天体重为j + B[i - 1]的计划数累加前一天计划数
                    dp[i][j + B[i - 1]] += dp[i - 1][j]
    # 最后一天非0天数
    return sum(dp[N])

# 读取输入
N, S, T = 2, 10, 20
A = [5,3]
B = [6,10]
# N, S, T = map(int, input().split())
# A = []
# B = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)

# 计算并输出结果
result = count_diet_plans(N, S, T, A, B)
print(result)
