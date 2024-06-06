# 1. build the char matrix
# 2. find the '.' position (first/last row/col can be ignored)
# 3. confirm if surround chars are '#'
# 4. yes, donuts count plus 1

row,col = map(int,input().split())
donuts_mat = [list(input()) for _ in range(row)]

count = 0

for i in range(1,row-1):
    for j in range(1,col-1):
        
        if donuts_mat[i][j] == '.':
            
            if donuts_mat[i][j-1] != '#':
                continue
            if donuts_mat[i-1][j-1] != '#':
                continue
            if donuts_mat[i-1][j] != '#':
                continue
            if donuts_mat[i][j+1] != '#':
                continue
            if donuts_mat[i+1][j] != '#':
                continue
            if donuts_mat[i+1][j+1] != '#':
                continue
            if donuts_mat[i-1][j+1] != '#':
                continue
            if donuts_mat[i+1][j-1] != '#':
                continue
            count += 1
            

print(count)