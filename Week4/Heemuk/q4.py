import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
a = t
b = t**1.8
c = t**3

plt.plot(t,a, 'r--')
plt.plot(t,b, 'gs')
plt.plot(t,c,'b^')
plt.show()
