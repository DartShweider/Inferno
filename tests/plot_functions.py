import math

import matplotlib.pyplot as plt

import numpy as np

# !!! Включаем интерактивный режим
plt.ion()

def graph_plot(*args, **kwargs):
    xlist = []
    ylist = []
    for i, arg in enumerate(args):
        if (i % 2 == 0):
            xlist.append(arg)
        else:
            ylist.append(arg)

    linewidth = kwargs.pop('linewidth', 1.)


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

