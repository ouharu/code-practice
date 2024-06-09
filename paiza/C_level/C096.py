# N = int(input())

# cal = [0]*31

# for _ in range(N):
#     start,end = map(int,input().split())
#     cal[start-1:end] = map(lambda x:x+1,cal[start-1:end])

# for day in cal:
#     if day >= N:
#         print('OK')
#         break
# else:
#     print('NG')

import numpy as np

N = int(input())

cal = np.zeros(31, dtype=int)

for _ in range(N):
    start, end = map(int, input().split())
    cal[start-1:end] += 1

if np.any(cal >= N):
    print('OK')
else:
    print('NG')
