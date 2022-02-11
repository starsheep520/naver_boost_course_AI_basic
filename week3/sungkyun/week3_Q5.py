import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1) # 기울기
bias = np.random.rand(1) # 절편

learning_rate = 0.01

for i in range(1000):
    pred = x_train * beta_gd + bias # 회귀식 예측값 y = Wx + b
    error = ((pred - y_train)**2).mean() # 평균제곱오차 MSE

    gradient_weight = (2*(pred - y_train)*x_train).mean() # Weight에 대한 편미분, 오차를 0으로 만들어야 함.
    gradient_bias = (2*(pred - y_train)).mean() # bias에 대한 편미분

    beta_gd = beta_gd - learning_rate*gradient_weight # beta_gd업데이트
    bias = bias - learning_rate*gradient_bias # bias 업데이트
    
    if i % 100 == 0:
        print('Epoch({:10d}/1000) error: {:10f}, beta_dg: {:10f}, bias: {:10f}'.format(i, error, beta_gd.item(), bias.item()))

