import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.,5.,0.2)
y = 4*t**2

plt.plot(t,y,'b^')
plt.plot(t,y/5,'gs')
plt.plot(t,y/25,'orange',linestyle = "dashed")
plt.plot()
plt.show()