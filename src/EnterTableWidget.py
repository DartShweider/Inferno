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
        self.load_And_Display_Button.clicked.connect(self.load_data_from_input_field)

    def load_data_from_input_field(self):
        from data_functions import create_data_arrays_from_str
        data_str = self.entry_Field_PlainText_Widget.toPlainText() + '\n'
        return create_data_arrays_from_str(data_str)

    def display_data(self):
        self.data_Table_Widget.clear()
            data_arrays = self.load_data_from_input_field()
            self.set_size_data_Table_Widget(data_arrays)
            self.fill_data_Table(data_arrays)

