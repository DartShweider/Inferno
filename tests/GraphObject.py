import sys
import os
import random
import matplotlib
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation


class My(FigureCanvas):
    def __init__(self, parent=None):
        style.use('fivethirtyeight')
        fig = plt.figure()
        self.ax1 = fig.add_subplot(1, 1, 1)
        FigureCanvas.__init__(self, fig)
        self.compute()

    def compute(self):
        xs = [1,5,78]
        ys = [6,9,3]
        self.ax1.clear()
        self.ax1.plot(xs, ys)


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        l = QtWidgets.QVBoxLayout(self)
        sc = My()
        l.addWidget(sc)


qApp = QtWidgets.QApplication(sys.argv)
aw = Window()
aw.show()
sys.exit(qApp.exec_())