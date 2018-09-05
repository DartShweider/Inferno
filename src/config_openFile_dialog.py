# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_openFile_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_openFile_Dialog(object):
    def setupUi(self, openFile_Dialog):
        openFile_Dialog.setObjectName("openFile_Dialog")
        openFile_Dialog.resize(433, 380)
        self.name_Of_Sheet_Label = QtWidgets.QLabel(openFile_Dialog)
        self.name_Of_Sheet_Label.setGeometry(QtCore.QRect(60, 140, 90, 18))
        self.name_Of_Sheet_Label.setObjectName("name_Of_Sheet_Label")
        self.cell_Range_LineEdit = QtWidgets.QLineEdit(openFile_Dialog)
        self.cell_Range_LineEdit.setGeometry(QtCore.QRect(240, 160, 141, 32))
        self.cell_Range_LineEdit.setObjectName("cell_Range_LineEdit")
        self.path_To_File_lineEdit = QtWidgets.QLineEdit(openFile_Dialog)
        self.path_To_File_lineEdit.setGeometry(QtCore.QRect(60, 80, 221, 32))
        self.path_To_File_lineEdit.setObjectName("path_To_File_lineEdit")
        self.name_Of_Sheet_LineEdit = QtWidgets.QLineEdit(openFile_Dialog)
        self.name_Of_Sheet_LineEdit.setGeometry(QtCore.QRect(60, 160, 141, 32))
        self.name_Of_Sheet_LineEdit.setObjectName("name_Of_Sheet_LineEdit")
        self.cell_Range_Label = QtWidgets.QLabel(openFile_Dialog)
        self.cell_Range_Label.setGeometry(QtCore.QRect(240, 140, 62, 18))
        self.cell_Range_Label.setObjectName("cell_Range_Label")
        self.path_To_File_Label = QtWidgets.QLabel(openFile_Dialog)
        self.path_To_File_Label.setGeometry(QtCore.QRect(70, 60, 28, 18))
        self.path_To_File_Label.setObjectName("path_To_File_Label")
        self.browse_Button = QtWidgets.QPushButton(openFile_Dialog)
        self.browse_Button.setGeometry(QtCore.QRect(300, 80, 84, 31))
        self.browse_Button.setMouseTracking(True)
        self.browse_Button.setObjectName("browse_Button")
        self.load_And_Display_Button = QtWidgets.QPushButton(openFile_Dialog)
        self.load_And_Display_Button.setGeometry(QtCore.QRect(140, 250, 151, 34))
        self.load_And_Display_Button.setObjectName("load_And_Display_Button")

        self.retranslateUi(openFile_Dialog)
        QtCore.QMetaObject.connectSlotsByName(openFile_Dialog)

    def retranslateUi(self, openFile_Dialog):
        _translate = QtCore.QCoreApplication.translate
        openFile_Dialog.setWindowTitle(_translate("openFile_Dialog", "Load file"))
        self.name_Of_Sheet_Label.setText(_translate("openFile_Dialog", "Name of sheet"))
        self.cell_Range_Label.setText(_translate("openFile_Dialog", "Cell range"))
        self.path_To_File_Label.setText(_translate("openFile_Dialog", "Path"))
        self.browse_Button.setText(_translate("openFile_Dialog", "Browse..."))
        self.load_And_Display_Button.setText(_translate("openFile_Dialog", "Load and display"))

