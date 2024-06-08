# https://paiza.jp/challenges/513/show

def check_int(input_str):
    try:
        # Convert the input string to an integer
        number = int(input_str)
        
        # Check if the number is within the range 0-100
        if 0 <= number <= 100:
            return number
        else:
            return '_'
    except ValueError:
        # Handle the case where the input is not a valid integer
        return '_'

def cal_mean(ques_lst:list) -> int:
    sum_ = 0
    i = 0
    for ques in ques_lst:
        if ques != '_':
            sum_ += ques
            i += 1
    # Has int in list
    if i != 0:
        return sum_ // i 
    # None int in list
    else:
        return 0

if __name__ == "__main__":
    ans_num, ques_num = map(int,input().split())
    survey_mat = [list(map(check_int, input().split()))for _ in range(ans_num)]
    for col in zip(*survey_mat):
        print(cal_mean(col))