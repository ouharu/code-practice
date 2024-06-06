# https://paiza.jp/career/challenges/572/
# 1. 找出最大值max 最小值min，min为最先出，max为最后出
# 2. 如果arr.index(max)<arr.index(min)，大数靠近出口 loop += 1
# 3. rotate数列使min在最前
# 4. pop min，更新最小值，重复2~3直到pop all items of list


def rotate_array(arr, min_):
    # 获取数组长度
    length = len(arr)

    # 找到min_ 的当前位置
    index_min = arr.index(min_)

    # 计算需要循环移动的步数
    steps = index_min - 0

    # 循环移动数组
    for _ in range(steps):
        # 将first元素移动到数组的开头
        first_element = arr.pop(0)
        arr.append(first_element)

    return arr


if __name__ == "__main__":

    # N = 5
    # A = [5, 2, 1, 3, 4]
    
    N = int(input())
    A = [int(input()) for _ in range(N)]
    
    max_ = max(A)
    loop = 0
    while len(A) > 1:
        min_ = min(A)
        if A.index(max_) < A.index(min_):
            loop += 1
        A = rotate_array(A, min_)
        A.pop(0)

    print(loop)
