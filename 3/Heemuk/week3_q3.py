import numpy as np
from sklearn.model_selection import train_test_split

xy = np.array([[1., 2., 3., 4., 5., 6.],
             [10., 20., 30., 40., 50., 60.]])

x_train, x_test, y_train, y_test = train_test_split(xy[0], xy[1], test_size=0.2)

print(x_train, x_train.shape)
print(y_train, y_train.shape)
