# input
# N = int(input())
# num_lst = [int(input()) for _ in range(N)]
# print(N,num_lst)

N = 5
num_lst = [5,2,1,3,4]
pop = 0


# *思路有问题
# 遍历数组，找出升序子序列，pop出去，pop次数+1，输出总pop次数
def find_sub_asdlst(num_lst:list)->list:
    idx = 0
    num_count = len(num_lst)
    res = []
    while idx < num_count - 1:
        if num_lst[idx] <= num_lst[idx+1]: 
            start = idx
            while idx+1 < num_count and num_lst[idx] <= num_lst[idx+1]:
                idx += 1
            end = idx
            res.extend(num_lst[start:end+1])
            
        idx += 1
    return res

while len(num_lst) > 0:
    
    arr = find_sub_asdlst(num_lst)

    if len(arr) == 0:
        num_lst.pop(0)
        pop += 1
    else:
        num_lst = [x for x in num_lst if x not in arr]
        pop += 1


# output
print(pop-1)

