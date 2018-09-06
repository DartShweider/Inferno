import math
import matplotlib.pyplot as plt
import numpy as np
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import config_graphSettings_dialog



class GraphSettingsDialog(QtWidgets.QMainWindow, config_graphSettings_dialog.Ui_GraphSettingsDialog):
    def __init__(self, parent = None):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_main_window.py
        super().__init__(parent)
        self.main = parent
        self.setupUi(self) #   Это нужно для инициализации нашего дизайна
        self.initActions()

    def initActions(self):
        self.set_axes_Plot_Table_size()
        self.create_plot_CheckBoxes()
        self.fill_axes_Plot_Table()

    def display_graph(self):
        pass

    def set_axes_Plot_Table_size(self):
        self.axes_Plot_Table_columns = self.main.data_Table_Widget.columnCount()
        if self.axes_Plot_Table_columns > 0:
            self.axes_Plot_Table.setRowCount((self.axes_Plot_Table_columns - 1) * 2)
        self.axes_Plot_Table.setColumnCount(self.axes_Plot_Table_columns)

    def create_plot_CheckBoxes(self):
        self.axes_Plot_Table_CheckBoxes = []
        for row in range((self.axes_Plot_Table_columns- 1)*2):
            self.axes_Plot_Table_CheckBoxes.append([])
            for column in range(self.axes_Plot_Table_columns):
                self.axes_Plot_Table_CheckBoxes[row].append(QtWidgets.QCheckBox())



    def fill_axes_Plot_Table(self):
        for row in range((self.axes_Plot_Table_columns - 1)*2):
            for column in range(self.axes_Plot_Table_columns):
                self.axes_Plot_Table.setCellWidget(row, column, self.axes_Plot_Table_CheckBoxes[row][column])
