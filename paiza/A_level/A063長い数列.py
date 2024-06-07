from typing import List
# from collections import deque
# def cal_lst(k_kind:int,lst:List[Tuple[int,int]]) -> int:
#     '''!!RUNTIME ERROR!! version'''
#     long_lst = []
#     for num,val in lst:
#         long_lst.extend([val]*num)
    
#     length = len(long_lst)
#     abs_sum = 0
#     for i in range(length//2):
#         abs_sum += abs(long_lst[i]-long_lst[length//2+i])

#     return abs_sum

# def cal_lst(k_kind:int,lst:List[Tuple[int,int]]) -> int:
#     '''!!RUNTIME ERROR!! cannot create a long list'''
#     lst_length = sum(tpl[0] for tpl in lst)
#     half_length = lst_length // 2
    
#     first_half = deque()
#     second_half = deque()
#     accumulate_num = 0
    
#     for num,val in lst:
#         accumulate_num += num
#         # 累计和未越过中线
#         if accumulate_num <= half_length:
#             first_half.extend([val]*num)
#         else:
#             sub = accumulate_num - half_length
#             # 完全越过
#             if sub >= num:
#                 second_half.extend([val]*(num))
#             else:
#                 second_half.extend([val]*(sub))
#                 first_half.extend([val]*(num - sub))

#     abs_sum = 0
#     for i in range(half_length):
#         abs_sum += abs(first_half[i]-second_half[i])

#     return abs_sum

def cal_lst(k_kind:int,lst:List[List[int]]) -> int:
    lst_length = sum(tpl[0] for tpl in lst)
    half_length = lst_length // 2
    
    first_half = []
    second_half = []
    accumulate_num = 0
    temp = [0,0]
    
    for num,val in lst:
        accumulate_num += num
        # 累计和未越过中线
        if accumulate_num <= half_length:
            first_half.append([num,val])
        else:
            # 越过个数 sub
            sub = accumulate_num - half_length
            second_half.append([sub,val])
            if num-sub != 0:
                first_half.append([num-sub,val])
            # 累计和过半，其余lst元素加入second_half
            accumulate_num = half_length
    count = 0
    abs_sum = 0
    while count < half_length:
        if temp == [0,0]:
            f = first_half.pop(0)
            s = second_half.pop(0)
        if f[0]>s[0]:
            small = s[0]
            abs_sum += small * abs(s[1]-f[1])
            temp = [f[0] - s[0] , f[1]]
            f = temp
            s = second_half.pop(0)
            count += small
        elif f[0]<s[0]:
            small = f[0]
            abs_sum += small * abs(s[1]-f[1])
            temp = [s[0] - f[0] , s[1]]
            s = temp
            f = first_half.pop(0)
            count += small
        elif f[0]==s[0]:
            small = f[0]
            abs_sum += small * abs(s[1]-f[1])
            temp = [0,0]
            count += small

    return abs_sum



# input
# k_kind = int(input())

# lst = [tuple(map(int,input().split())) for _ in range(k_kind)]

k_kind = 4
lst = [[2,1],[4,7],[3,1],[1,3]]

print(cal_lst(k_kind,lst))