<<<<<<< HEAD
from optparse import Values
import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'groub_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))

plt.subplot(1,3,1)
plt.bar(names, values)

plt.subplot(1,3,2)
plt.scatter(names, values)

plt.subplot(1,3,3)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
=======
from optparse import Values
import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'groub_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))

plt.subplot(1,3,1)
plt.bar(names, values)

plt.subplot(1,3,2)
plt.scatter(names, values)

plt.subplot(1,3,3)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
>>>>>>> 1cd0b0ddf18224d14fbbee1430d43df0883cff73
plt.show()