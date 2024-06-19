# python中的字典解析

## Syntax

` {key: value for key,value in iterable if condition}`

## Problem

以下程序中，dict通过字典解析生成，通过if条件来限制多个key导致对应value被反复赋值,即如果dict中key不存在才能添加，结果key对应value依旧被更新为最新。

```python
# N= int(input())
N = 4
# num_lst = [int(input()) for _ in range(N)]
num_lst = [12,5,36,12]

sorted_lst = sorted(num_lst,reverse=True)
ranking_dict = {}
ranking_dict = {num:(idx+1) for idx,num in enumerate(sorted_lst) if num not in ranking_dict}

for i in range(N):
    print(ranking_dict[num_lst[i]])
```

## 原因

if not in ranking_dict中对比的字典为初始的空字典，导致一直符合if条件，若无空字典初始化，将报错。

## 解决

1. 将enumerate(sorted_lst)反向遍历，重复值的idx最终为最小值（最先出现的值）

```python
# N= int(input())
N = 4
# num_lst = [int(input()) for _ in range(N)]
num_lst = [12,5,36,12]
num_len = len(num_lst)
# 升序排列
sorted_lst = sorted(num_lst) 
# 升序需要反向排名
ranking_dict = {num:(num_len-idx) for idx,num in enumerate(sorted_lst)}

for i in range(N):
    print(ranking_dict[num_lst[i]])
```

2. for循环更新dict，每次对num是否是dict的key进行判断

```python
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
```
