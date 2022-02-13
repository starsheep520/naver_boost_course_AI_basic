import matplotlib.pyplot as plt

names = ['group_a','group_b','group_c']
values = [1,10,100]

fig = plt.figure()
fig.set_size_inches(10,5)

bar = fig.add_subplot(1,3,1)
dot = fig.add_subplot(1,3,2)
line = fig.add_subplot(1,3,3)

bar.bar(names,values)
dot.scatter(names,values)
line.plot(names,values)

plt.show()