# ・誤差 5 Hz 以内なら減点しない
# ・上記に当てはまらず、誤差 10 Hz 以内なら 1 点減点
# ・上記に当てはまらず、誤差 20 Hz 以内なら 2 点減点
# ・上記に当てはまらず、誤差 30 Hz 以内なら 3 点減点
# ・上記に当てはまらない場合、5 点減点

def minus_score(right_hz:int,input_hz:int) -> int:
    error = abs(right_hz-input_hz)
    if error<=5:
        return 0
    elif error<=10:
        return -1
    elif error<=20:
        return -2
    elif error<=30:
        return -3
    else:
        return -5        

def cmp(template_hz:list,human_hz:list) -> int:
    max_score = 0
    for one_hz in human_hz:
        # point: initiate the variable in the certain position
        one_score = 100
        for right_hz,input_hz in zip(template_hz,one_hz):
            one_score += minus_score(right_hz,input_hz)
            if one_score < 0:
                one_score = 0 
                break    
        max_score = max(max_score,one_score)
    return max_score

N,M = map(int, input().split())

template_hz = [int(input()) for _ in range(M)]
human_hz = [[int(input()) for _ in range(M)] for _ in range(N)]

print(cmp(template_hz,human_hz))