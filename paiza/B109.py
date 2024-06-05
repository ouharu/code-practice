# 1.找出所有未预约not_res_pos与best_pos距离
# 2.返回里面最小距离所在下标

# input
N, H, W, P, Q = list(map(int,input().split()))
res_pos = [tuple(map(int,input().split())) for _ in range(N)]

# 求与P，Q曼哈顿距离最小的位置坐标
min_dist = H*W
min_pos = []

for i in range(H):
    for j in range(W):
        if (i,j) not in res_pos:
            dist = abs(i-P) + abs(j-Q)
            if dist < min_dist:
                min_dist = dist
                min_pos =[(i,j)]
            elif dist == min_dist:
                min_pos.append((i,j))

for x,y in min_pos:
    print(x,y)