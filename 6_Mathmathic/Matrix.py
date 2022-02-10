import numpy as np

# 행렬(Matrix) : 벡터를 원소로 가지는 2차원 행렬
X = np.array([[1, -2, 3],
              [7, 5, 0],
              [-2, -1, 2]])

Y = np.array([[0,1],
              [1, -1],
              [-2, 11]])

Z = np.reshape(Y, (2,3))

# 행렬의 곱셈(Matrix Multiplication)
# i번째 행 벡터와 j번째 열벡터 사이의 내적
result_matrix_multi = X @ Y
print(result_matrix_multi)

# np.inner는 i번째 행 벡터와 j번째 행 벡터 사이의 내적을 성분으로 가지는 행렬을 계산
result_matrix_inner = np.inner(X, Z)
print(result_matrix_inner)

print(np.inner([1,-1,1,-1], [4,-4,4,-4]))

# 역행렬(Inverse Matirx)
inverse_matrix = np.linalg.inv(X)
determinant = X @ inverse_matrix

print(inverse_matrix)
print(determinant) 

# 유사역핵렬
pseudo_inverse_matrix = np.linalg.pinv(Y)
pseudo_determinant = pseudo_inverse_matrix @ Y

print(pseudo_inverse_matrix)
print(pseudo_determinant)