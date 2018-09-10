import math

import matplotlib.pyplot as plt

import numpy as np

# !!! Включаем интерактивный режим


#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.grid(True)


def plot_function(data_arrays):
    plt.ion()
    plt.grid(True)

    for graph in range(len(data_arrays)):

        plt.scatter(data_arrays[graph].array_X, data_arrays[graph].array_Y)
            # !!! Нарисуем их
            # !!! Обратите внимание, что здесь используется функция draw(), а не show()
        plt.draw()
        plt.plot(data_arrays[graph].array_X, data_arrays[graph].array_Y)
    plt.ioff()
    plt.show()


def f_plot(*args, **kwargs):
    xlist = []
    ylist = []
    for i, arg in enumerate(args):
        if (i % 2 == 0):
            xlist.append(arg)
        else:
            ylist.append(arg)

    colors = kwargs.pop('colors', 'k')
    linewidth = kwargs.pop('linewidth', 1.)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    i = 0
    for x, y, color in zip(xlist, ylist, colors):
        i += 1
        ax.plot(x, y, color=color, linewidth=linewidth, label=str(i))

    ax.grid(True)
    ax.legend()
    plt.show()


