from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets


import config_options_dialog

class OptionsDialog(QtWidgets.QDialog, config_options_dialog.Ui_OptionsDialog):
    def __init__(self, parent = None):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_options_dialog.py
        super().__init__(parent)
        self.initUi()
    def initUi(self):
        self.setupUi(self)
