# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_enterTable_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_enter_Table_Widget(object):
    def setupUi(self, enter_Table_Widget):
        enter_Table_Widget.setObjectName("enter_Table_Widget")
        enter_Table_Widget.resize(538, 412)
        self.entry_Field_PlainText_Widget = QtWidgets.QPlainTextEdit(enter_Table_Widget)
        self.entry_Field_PlainText_Widget.setGeometry(QtCore.QRect(90, 100, 311, 261))
        self.entry_Field_PlainText_Widget.setObjectName("entry_Field_PlainText_Widget")
        self.input_Label = QtWidgets.QLabel(enter_Table_Widget)
        self.input_Label.setEnabled(True)
        self.input_Label.setGeometry(QtCore.QRect(220, 80, 41, 18))
        self.input_Label.setObjectName("input_Label")
        self.load_And_Display_Button = QtWidgets.QPushButton(enter_Table_Widget)
        self.load_And_Display_Button.setGeometry(QtCore.QRect(340, 30, 151, 34))
        self.load_And_Display_Button.setObjectName("load_And_Display_Button")

        self.retranslateUi(enter_Table_Widget)
        QtCore.QMetaObject.connectSlotsByName(enter_Table_Widget)

    def retranslateUi(self, enter_Table_Widget):
        _translate = QtCore.QCoreApplication.translate
        enter_Table_Widget.setWindowTitle(_translate("enter_Table_Widget", "Enter table"))
        self.input_Label.setText(_translate("enter_Table_Widget", "Input"))
        self.load_And_Display_Button.setText(_translate("enter_Table_Widget", "Load and display"))

