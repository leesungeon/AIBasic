# 미분(differentitation)
# 변수의 움직임에 따른 함수값의 변화를 측정하기 위한 도구
import numpy as np
import sympy as sym
from sympy.abc import x,y

result = sym.diff(sym.poly(x**2 + 2*x + 3), x)
print(result)

# 미분은 접선의 기울기를 구한다
# 한 점에서 접선의 기울기를 알면 어느 방향으로 점을 움직여야 함수값이 증가/감소 하는 지 알 수 있다.
# 증가시키고 싶다면 -> 미분 값을 더한다.
# 감소시키고 싶다면 -> 미분 값을 뺀다.

# 미분 값을 더하면 경사상승법(gradient ascent)이라 하며 함수의 극대값의 위치를 구함
# 미분 값을 빼면 경사하강법(gradient descent)이라 하며 함수의 극소값의 위치를 구함
# 극값에 도달하면 움직임을 멈춘다

# 경사하강법 (gradient descent)
# gradient : 그레이언트 벡터 (or 미분)을 계산하는 함수
# init : 시작점, lr : 학습률, eps : 알고리즘 종료 조건, var : output
def eval_(fun, val):
    val_x, val_y = val
    fun_eval = fun.subs(x, val_x).subs(y, val_y)
    return fun_eval

def func_multi(val):
    x_, y_ = val
    func = sym.poly(x**2 + 2*y**2)
    return eval_(func, [x_,y_]), func

def func_gradient(fun, val):
    x_, y_ = val
    _, function = fun(val)
    diff_x = sym.diff(function, x)
    diff_y = sym.diff(function, y)
    grad_vec = np.array([eval_(diff_x, [x_, y_]), eval_(diff_y, [x_, y_])], dtype=float)
    return grad_vec, [diff_x, diff_y]

def gradient_descent(fun, init_point, lr_rate=0.01, epsilon=0.00001):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(fun, init_point)
    while np.linalg.norm(diff) > epsilon:
        val = val - lr_rate*diff
        diff, _ = func_gradient(fun, val)
        cnt += 1
    
    print("함수: {}, 연산횟수: {}, 최소점: ({}, {})".format(fun(val)[1], cnt, val, fun(val)[0]))

gradient_descent(fun=func_multi, init_point=np.random.uniform(-2,2))
# 변수가 벡터인 경우 : 편미분(partial differentitation)을 사용
# 각 변수 별로 편미분을 계산한 그레디언트(gradient) 벡터를 이용하여 경사하강/상승법에 사용 가능
