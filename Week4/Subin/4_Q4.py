import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

#예시코드 참조
plt.plot(t, t, 'r--', t, t**2, 'gs', t, t**3, 'b^')


plt.show()