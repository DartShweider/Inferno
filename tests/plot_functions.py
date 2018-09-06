import math

import matplotlib.pyplot as plt

import numpy as np

# !!! Включаем интерактивный режим
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)


def plot_function(xList, yList):

    plt.grid(True)
    for x, y in zip(xList, yList):
        plt.plot(x, y)
        plt.scatter(x, y)
        # !!! Нарисуем их
        # !!! Обратите внимание, что здесь используется функция draw(), а не show()
        plt.draw()

plt.ioff()
plt.show()

