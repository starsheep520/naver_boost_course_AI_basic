import matplotlib.pyplot as plt


#5

import matplotlib.pyplot as plt
import numpy as np

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

#plt.figure: 새로운 figure 생성
plt.figure(figsize =(9,3))

#막대그래프
plt.bar(names, values,)

#점 그래프
plt.figure()
plt.scatter(names, values)

#선 그래프
plt.figure()
plt.plot(names, values)

plt.show()

#데이터 라벨이 미표기되는 문제
