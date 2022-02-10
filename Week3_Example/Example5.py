import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
              [3., 6., 9., 12., 15., 18.]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.01

for i in range(1000):
    prediction = (x_train * beta_gd) + bias
    error = ((prediction - y_train) ** 2).mean()

    w = ((prediction - y_train) * 2 * x_train).mean()
    b = ((prediction - y_train) * 2).mean()

    beta_gd -= learning_rate * w
    bias -= learning_rate * b

    if i % 100 == 0:
        print('Epoch({:10d}/1000) error : {:10f}, bias: {:10f}'.format(i, error, beta_gd.item(), bias.item()))