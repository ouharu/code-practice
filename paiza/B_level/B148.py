# N= int(input())
N = 4
# num_lst = [int(input()) for _ in range(N)]
num_lst = [12,5,36,12]
# num_len = len(num_lst)
sorted_lst = sorted(num_lst,reverse=True)

# approach 1
# ranking_dict = {num:(num_len-idx) for idx,num in enumerate(sorted_lst)}
# approach 2
ranking_dict = {}
for idx,num in enumerate(sorted_lst):
    if num not in ranking_dict:
        ranking_dict[num] = idx + 1

for i in range(N):
    print(ranking_dict[num_lst[i]])