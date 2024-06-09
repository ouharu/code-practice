import numpy as np 

row, col = map(int,input().split())
mat = [list(map(str,input())) for _ in range(row)]

bumb_row = np.zeros(row,dtype=bool)
bumb_col = np.zeros(col,dtype=bool)

for i in range(row):
    for j in range(col):
        if mat[i][j] == '#':
            bumb_row[i] = True
            bumb_col[j] = True

print(sum(bumb_col)*row + sum(bumb_row)*col - sum(bumb_row)*sum(bumb_col))