#Test program

import matplotlib.pyplot as plt
import math
import numpy as np


arr_x, arr_y  = [], []




while True:
    a = input().split()
    if a == ['go']:
        flag = False
        break
    arr_x.append(float(a[0]))
    arr_y.append(float(a[1]))



def plot(x, y, **kwargs):
    plt.plot(x, y, **kwargs)

def scatter(x, y):
    plt.scatter(x, y)



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

    x = np.arange(min(arr_x), max(arr_x))
    y = b*x + a

    plt.plot(x, y, color = 'green')

    return


def approx_exp(arr_x, arr_y):
    N = len(arr_x)
    sum_lny = 0
    sum_x_square = 0
    sum_lny_x = 0
    sum_x = 0

    for i in range(N):
        if arr_y[i]!=0:
            sum_lny += math.log(arr_y[i])
            sum_lny_x += math.log(arr_y[i]) * arr_x[i]
        sum_x_square += arr_x[i] ** 2

        sum_x += arr_x[i]
    ln_a = (sum_lny * sum_x_square - sum_lny_x * sum_x) / (N * sum_x_square - sum_x ** 2)
    b = (N * sum_lny_x - sum_lny * sum_x) / (N * sum_x_square - sum_x ** 2)
    a = math.exp(ln_a)
    x = np.arange(min(arr_x), max(arr_x))
    y = a*np.exp(b*x)

    print('a = ', a, 'b = ', b)

    plt.plot(x, y, color='red')


graph_plot(arr_x, arr_y, colour = 'blue')
approx_line(arr_x, arr_y)
approx_exp(arr_x, arr_y)
plt.grid(True)

plt.show()

