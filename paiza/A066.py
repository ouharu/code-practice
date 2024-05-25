# process
def max_consecutive_workdays(intervals):
    current_end = intervals[0][1]
    current_consecutive_workdays = current_end - intervals[0][0] + 1
    max_workdays = current_consecutive_workdays

    for start, end in intervals[1:]:
        if start > current_end + 1:
            # 不连续
            current_consecutive_workdays = end - start + 1
            current_end = end
        else:
            # 连续，判断包含关系
            if end >= current_end:
                current_consecutive_workdays += end - current_end
                current_end = end
        max_workdays = max(max_workdays, current_consecutive_workdays)

    return max_workdays

# input
N = int(input())

intervals = [tuple(map(int, input().split())) for _ in range(N)]
intervals.sort(key=lambda interval: interval[0])
# print(intervals)
# output
print(max_consecutive_workdays(intervals))
print()
