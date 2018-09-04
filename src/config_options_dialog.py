# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_options_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.setWindowModality(QtCore.Qt.NonModal)
        OptionsDialog.resize(506, 486)
        self.pushButton = QtWidgets.QPushButton(OptionsDialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 150, 88, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(OptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        OptionsDialog.setWindowTitle(_translate("OptionsDialog", "Options"))
        self.pushButton.setText(_translate("OptionsDialog", "PushButton"))

