import numpy as np

# 경사하강법 기반의 선형회귀 알고리즘
# 목적식을 최소화하는 베타(b)를 찾아야 하므로 그레디언트 벡터를 구해야 함
#np.linalg.norm
x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(x, np.array([1, 2])) + 3

beta_gd = [10.1, 15.1, -6.5]
x_ = np.array([np.append(x, [1]) for _x in x])

for t in range(5000):
    error = y - x_ @ beta_gd
    grad = - np.transpose(x_) @ error
    beta_gd = beta_gd - 0.01 * grad

print(beta_gd)