#Main program

import matplotlib.pyplot as plt

import numpy as np


arr_x, arr_y  = [], []

a = input().split()


while a[0] != 'go':

    arr_x.append(float(a[0]))
    arr_y.append(float(a[1]))
    a = input().split()





def f_plot(*args, **kwargs):
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
    i = 0
    for x, y in zip(xlist, ylist):
        i += 1
        plt.scatter(x, y)
        plt.plot(x, y, linewidth=linewidth, label=str(i))

    ax.grid(True)
    ax.legend()



def approx_line(arr_x, arr_y):
    x_1 = 0
    x_2 = 0
    y_1 = 0
    y_2 = 0
    x_y = 0
    N = len(arr_x)
    for i in range(N):
        x_1 = x_1 * (i / (i + 1)) + arr_x[i] / (i + 1)
        x_2 = x_2 * (i / (i + 1)) + (arr_x[i] ** 2) / (i + 1)
        y_1 = y_1 * (i / (i + 1)) + arr_y[i] / (i + 1)
        y_2 = y_2 * (i / (i + 1)) + (arr_y[i] ** 2) / (i + 1)
        x_y = x_y * (i / (i + 1)) + (arr_x[i] * arr_y[i]) / (i + 1)
    b = (x_y - (x_1 * y_1)) / (x_2 - (x_1 ** 2))
    a = y_1 - b * x_1
    n = 1 / (N ** 0.5)
    sig_b = n * ((((y_2 - (y_1 ** 2))/(x_2 - (x_1 ** 2))) - (b ** 2)) ** 0.5)
    sig_a = sig_b * ((x_2 - (x_1 ** 2)) ** 0.5)
    print("x: ", x_1,"x^2: ", x_2, "y: ", y_1,"y^2: ", y_2,"x * y:", x_y)
    print('y = a + bx, где a = ', a, ' +- ', sig_a, ' b = ', b, ' +-', sig_b)

    x = np.arange(300)
    y = b*x + a

    plt.plot(x, y, color = 'green')
f_plot(arr_x, arr_y)

approx_line(arr_x, arr_y)

plt.grid(True)

plt.show()
