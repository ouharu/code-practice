# 入力例1
# 3 5
# 3 7 4 5 1
# 6 9 1 8 8
# 11 2 5 2 2

row,col = map(int,input().split())
choco_mat = [list(map(int,input().split())) for _ in range(row)]

# row,col = 3,5
# choco_mat = [[3,7,4,5,1],[6,9,1,8,8],[11,2,5,2,2]]

split_mat = []
row_count = 0
for choco_row in choco_mat:
    alice = 0
    sum_ = 0
    mean = sum(choco_row) // 2
    for choco in choco_row:
        sum_ += choco
        alice += 1
        if mean == sum_:
            split_mat.append('A'*alice+'B'*(col-alice))
            row_count += 1
            break
if row_count == row:
    print('Yes')
    print(*split_mat,sep='\n')
else:
    print('No')

# print(row,col,choco_mat)