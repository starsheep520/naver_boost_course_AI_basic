import numpy as np

x = np.random.rand(5, 3)
y = np.random.rand(3, 2)
cal = np.dot(x, y)
print(cal, cal.shape)
