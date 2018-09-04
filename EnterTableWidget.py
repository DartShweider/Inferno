from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets


import config_enterTable_widget

class EnterTableWidget(QtWidgets.QDialog, config_enterTable_widget.Ui_enter_Table_Widget):
    def __init__(self, parent = None):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_options_dialog.py
        super().__init__(parent)
        self.initUi()
    def initUi(self):
        self.setupUi(self)
