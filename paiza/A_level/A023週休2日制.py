# 计算一个数组中实现7个元素中至少有2个0的子数组连续出现的最大长度 max
# 1.用len(windows)=7的滑动窗口去捕捉子数组（7elements, 0 element >= 2）
# 2. window: [start,start+7) , start+7 <= num
# 3.子数组符合条件(current consecutive days = 7 )/不符合(=0),滑动到下一元素
# 4.子数组符合条件(current consecutive days += 1 )/不符合(=0 断了),滑动到下一元素
# 3. 4.区别在于前一次是否有连续(>=7)


def max_2day_weekend_schedule(num:int,schedule:list)->int:
    current_consecutive_days = 0
    max_consecutive_days = 0

    for i in range(num):
        start = i    
        end = start + 7
        if end > num:
            break
        if sum(schedule[start:end])<= 5:
            if current_consecutive_days >= 7:
                current_consecutive_days += 1
            else:
                current_consecutive_days = 7
        else:
            current_consecutive_days = 0
        max_consecutive_days = max(max_consecutive_days,current_consecutive_days)

    return max_consecutive_days
    
num = int(input())

schedule = list(map(int,input().split()))

print(max_2day_weekend_schedule(num,schedule))