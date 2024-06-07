# Input:
# num_kind = int(input())
# num_lst = [int(input()) for _ in range(2*num_kind)]

# Temp Variable:
# find_num_lst = []
# gap = 0

# !!TIME OUT!!: list.index O(n)
# while(len(find_num_lst)<=num_kind and len(num_lst) >= 1):
#     num = num_lst.pop(0)
#     if num not in find_num_lst:
#         find_num_lst.append(num)
#         gap += num_lst.index(num)

def gap_sum(n:int,lst:list) -> int:
    gap = 0
    find_num_lst = {}

    for idx,num in enumerate(lst):
        # find_num_lst for saving num and idx in the first occurrence.
        if num in find_num_lst:
            gap += (idx-find_num_lst[num]-1)
            # exit the loop prematurely
            n -= 1
            if n == 0:
                break
        else:
            find_num_lst[num] = idx
    return gap



# Input:
num_kind = int(input())
num_lst = [int(input()) for _ in range(2*num_kind)]

print(gap_sum(num_kind,num_lst))