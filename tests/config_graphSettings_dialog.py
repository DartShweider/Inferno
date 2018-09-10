# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_graphSettings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GraphSettingsDialog(object):
    def setupUi(self, GraphSettingsDialog):
        GraphSettingsDialog.setObjectName("GraphSettingsDialog")
        GraphSettingsDialog.resize(527, 422)
        self.axes_Plot_Table = QtWidgets.QTableWidget(GraphSettingsDialog)
        self.axes_Plot_Table.setGeometry(QtCore.QRect(120, 40, 371, 161))
        self.axes_Plot_Table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.axes_Plot_Table.setRowCount(0)
        self.axes_Plot_Table.setColumnCount(0)
        self.axes_Plot_Table.setObjectName("axes_Plot_Table")
        self.plot_Button = QtWidgets.QPushButton(GraphSettingsDialog)
        self.plot_Button.setGeometry(QtCore.QRect(300, 270, 81, 34))
        self.plot_Button.setObjectName("plot_Button")

        self.retranslateUi(GraphSettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(GraphSettingsDialog)

    def retranslateUi(self, GraphSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        GraphSettingsDialog.setWindowTitle(_translate("GraphSettingsDialog", "Graph settings"))
        self.plot_Button.setText(_translate("GraphSettingsDialog", "Plot"))

