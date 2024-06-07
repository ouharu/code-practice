# 4 5
# 2 0 0 0 1
# 0 2 0 0 0
# 0 1 0 3 0
# 0 0 1 0 0
# 2 3
# ##.
# #.#

# input
sea_row , sea_col = map(int,input().split())
sea_mat = [list(map(int,input().split())) for _ in range(sea_row)]

net_row , net_col = map(int,input().split())
net_mat = [list(map(str,input())) for _ in range(net_row)]
net_mat = [[1 if x=='#' else 0 for x in row]for row in net_mat]

# mat slide
max_fish = 0 
# sea_net = [[0]*net_col for _ in range(net_row)]
for i in range(sea_row):
    r_start = i
    r_end = r_start + net_row
    if r_end > sea_row:
        break
    for j in range(sea_col):
        c_start = j
        c_end = c_start + net_col
        if c_end > sea_col:
            break
        sea_net = [row[c_start:c_end] for row in sea_mat[r_start:r_end]]
        res = 0
        for r in range(net_row):
            for c in range(net_col):
                res += sea_net[r][c]*net_mat[r][c]
        max_fish = max(res,max_fish)
print(max_fish)