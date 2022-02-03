# Vector
# 숫자를 원소로 가지는 리스트(list) 또는 배열(array)
# 벡터는 원점으로부터 상대적 위치를 표현합니다

import numpy as np

x = np.array([1,7,2])
y = np.array([5,2,1])

# 같은 모양을 가지면 덧셈, 뺄셈을 계산할 수 있음.
result_1 = x + y
print(result_1)

# 같은 모양을 가지면 성분곱(Hadamard product)을 할 수 있음
result_2 = x * y
print(result_2)

# 벡터의 노름(norm)은 원점에서부터의 거리를 말합니다.
# L1-노름은 각 성분의 변화량의 절대값을 모두 더합니다.
def l1_norm(x):
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm

# L2-노름은 피타고라스 정리를 이용해 유클리드 거리를 계산
# l2-노름은 np.linalg.norm을 이용해도 구현 가능하다.
def l2_norm(x):
    x_norm = x*x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm

# 두 벡터 사이의 각도
def angle(x,y):
    v = np.inner(x, y) / (l2_norm(x) + l2_norm(y))
    theta = np.arccos(v)
    return theta
