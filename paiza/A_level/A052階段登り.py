# https://paiza.jp/challenges/462/show

# N = int(input())
# A,B = map(int,input().split())

# N = 15
# A,B = 4,6

# if A>B:
#     A,B = B,A

# steps = [0]*(N+1) 

# i,j = 0,0
# 1. 没读懂题意，每次前进A或者B，并非一直A或B
# while True:
#     if i <= N and j <=N :
#         steps[i] = 1
#         i += A
#         steps[j] = 1        
#         j += B
#     elif i <= N and j > N :
#         steps[i] = 1
#         i += A
#     elif i > N and j > N :
#         steps[-1] = 1
#         break


# sum_ = 0
# for step in steps:
#     if step == 0:
#         sum_ += 1
# print(sum_)

# 2. 这道题转化为二叉树问题： (可以解决，但是创建list占用内存导致runtime error)
# 例：N=8 A，B = 3，5
# 可生成二叉树：
# 0
# 3 5
# 6 8 8 10
# 可知数值表示接触到的地板：0，3，5，6，8
# 层数2层由N//A决定
# 每层看作一个列表，由上一个列表数字分别加上A，B得到

# N = int(input())
# A,B = map(int,input().split())

# # N = 15
# # A,B = 4,6

# if A>B:
#     A,B = B,A

# def generate_lst(lst,A,B):
#     res = []
#     for num in lst:
#         res.append(num + A)
#         res.append(num + B)
#     return res

# jump = 0
# jumped_lst = [0]
# jumped_set = {0}
# while (jump<N//A):
#     jumped_lst = generate_lst(jumped_lst,A,B)
#     # set() removed duplicated items
#     jumped_set.update(jumped_lst)
#     jump += 1

# jumped_set = list(jumped_set)
# # only jump steps < N and final step N need to be jumped
# jumped_set = [x for x in jumped_set if x < N] + [N]
# print(N+1 - len(jumped_set))

# 3.朴素法： stair = i*A + j*B
# 缺点： 2次遍历
# def count_unreachable_stairs(N, A, B):
#     # Create a set to store the reachable stairs
#     reachable = set()
#     for i in range(N // A + 1 ):
#         for j in range(N // B + 1 ):
#             stair = i * A + j * B
#             if stair < N:
#                 reachable.add(stair)
#     # Count the number of unreachable stairs
#     return N - len(reachable)

# N = int(input())
# A, B = map(int, input().split())
# print(count_unreachable_stairs(N, A, B))

# AC
N = int(input())
A,B = map(int,input().split())

def count_unreachable_stairs(N,A,B):
    reachable = [False]*(N+1)
    reachable[0] = True
    reachable[-1] = True
    
    for i in range(1,N+1):
        if i>=A and reachable[i-A]==True:
            reachable[i] = True
        if i>=B and reachable[i-B]==True:
            reachable[i] = True
    # Count the number of unreachable stairs
    # Do not forget the last stair
    return N+1 - sum(reachable)

print(count_unreachable_stairs(N,A,B))