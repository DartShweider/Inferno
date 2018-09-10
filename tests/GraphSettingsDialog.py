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
        self.plot_Button.clicked.connect(self.display_graph)
        self.graphs = []

    def creation_graphs(self):
        self.graphs = []
        self.number_of_graphs = (int(self.axes_Plot_Table.rowCount() / 2))
        for number_checkBoxes_array in range(self.number_of_graphs):
            index_array_X = self.check_plot_CheckBoxes(self.axes_Plot_Table_CheckBoxes[number_checkBoxes_array * 2])
            index_array_Y = self.check_plot_CheckBoxes(self.axes_Plot_Table_CheckBoxes[(number_checkBoxes_array + 1) * 2 - 1])
            if index_array_Y == None or index_array_X == None:
                continue
            else:
                self.graphs.append(graph_object(self.main.main_data_arrays[index_array_X], self.main.main_data_arrays[index_array_Y]))

    def display_graph(self):
        self.creation_graphs()
        import plot_functions
        plot_functions.plot_function(self.graphs)

    def set_axes_Plot_Table_size(self):
        self.axes_Plot_Table_columns = self.main.data_Table_Widget.columnCount()
        if self.axes_Plot_Table_columns > 0:
            self.axes_Plot_Table.setRowCount((self.axes_Plot_Table_columns - 1) * 2)
        self.axes_Plot_Table.setColumnCount(self.axes_Plot_Table_columns)

    def set_axes_Plot_Table_Vertical_Headers(self):
        for row in range(int(self.axes_Plot_Table.rowCount()/2)):
            self.axes_Plot_Table.setVerticalHeaderItem(row * 2, QTableWidgetItem('Graph_'f'{row + 1}''(X)'))
            self.axes_Plot_Table.setVerticalHeaderItem((row + 1) * 2 - 1, QTableWidgetItem('Graph_'f'{row + 1}''(Y)'))

    def create_plot_CheckBoxes(self):
        self.axes_Plot_Table_CheckBoxes = []
        for row in range((self.axes_Plot_Table_columns- 1)*2):
            self.axes_Plot_Table_CheckBoxes.append([])
            for column in range(self.axes_Plot_Table_columns):
                self.axes_Plot_Table_CheckBoxes[row].append(QtWidgets.QCheckBox())

    def check_plot_CheckBoxes(self, array_CheckBoxes):
        for checkBox in array_CheckBoxes:
            if checkBox.isChecked() == True:
                return array_CheckBoxes.index(checkBox)

    def fill_axes_Plot_Table(self):
        for row in range((self.axes_Plot_Table_columns - 1)*2):
            for column in range(self.axes_Plot_Table_columns):
                self.axes_Plot_Table.setCellWidget(row, column, self.axes_Plot_Table_CheckBoxes[row][column])
        self.set_axes_Plot_Table_Vertical_Headers()


class graph_object():
    def __init__(self, array_X, array_Y):
        self.array_X = array_X
        self.array_Y = array_Y