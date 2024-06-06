import random

def generate_problems(problems:set,num:int,type_:str)->set:
    while len(problems) < num:
        a = random.randint(0, 99)
        # 和不超过99
        if type_ == '+':
            b = random.randint(0, 99-a)
            problem = f"{a} + {b} ="
        # 差大于等于0
        elif type_ == '-':
            b = random.randint(0, a)
            problem = f"{a} - {b} ="
        
        if problem not in problems:
            problems.add(problem)
    return problems

def generate_drills(M, N):
    addition_problems = set()
    subtraction_problems = set()

    addition_problems = generate_problems(addition_problems,M,'+')
    subtraction_problems = generate_problems(subtraction_problems,N,'-')
    
    drills = list(addition_problems) + list(subtraction_problems)
    random.shuffle(drills)

    return drills

# 读取输入
M, N = map(int, input().split())

# 生成计算练习题
drills = generate_drills(M, N)

# 输出结果
for problem in drills:
    print(problem)
